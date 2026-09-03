#!/usr/bin/env python3
"""Pull new PDFs from a Zotero collection into 01_Corpus/ (the drop zone).

Config lives outside the repo (the repo is public):
  ~/.config/thesis-zotero.env
    ZOTERO_USER_ID=1234567
    ZOTERO_API_KEY=xxxxxxxx
    ZOTERO_COLLECTION=Thesis
"""
import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

CONFIG = Path.home() / ".config" / "thesis-zotero.env"
CORPUS = Path(__file__).resolve().parent.parent / "01_Corpus"
STATE_FILE = CORPUS / ".zotero_state.json"
API = "https://api.zotero.org"

STOPWORDS = {"a", "an", "the", "on", "of", "for", "in", "and", "to", "with",
             "via", "by", "using", "toward", "towards", "from", "into"}


def die(msg):
    print(f"error: {msg}", file=sys.stderr)
    sys.exit(1)


def load_config():
    if not CONFIG.exists():
        die(f"missing config file {CONFIG}\n"
            "create it with:\n"
            "  ZOTERO_USER_ID=<your numeric userID>\n"
            "  ZOTERO_API_KEY=<your key>\n"
            "  ZOTERO_COLLECTION=Thesis")
    cfg = {}
    for line in CONFIG.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            cfg[k.strip()] = v.strip()
    for k in ("ZOTERO_USER_ID", "ZOTERO_API_KEY"):
        if not cfg.get(k):
            die(f"{k} not set in {CONFIG}")
    cfg.setdefault("ZOTERO_COLLECTION", "Thesis")
    return cfg


def api_get(cfg, path, raw=False):
    req = urllib.request.Request(
        f"{API}/users/{cfg['ZOTERO_USER_ID']}{path}",
        headers={"Zotero-API-Key": cfg["ZOTERO_API_KEY"]})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            data = r.read()
    except urllib.error.HTTPError as e:
        hint = " (bad or unauthorized API key?)" if e.code == 403 else ""
        die(f"Zotero API returned {e.code} for {path}{hint}")
    except urllib.error.URLError as e:
        die(f"cannot reach api.zotero.org: {e.reason}")
    return data if raw else json.loads(data)


def paged(cfg, path):
    start = 0
    while True:
        batch = api_get(cfg, f"{path}?limit=100&start={start}")
        yield from batch
        if len(batch) < 100:
            return
        start += 100


def find_collection(cfg):
    name = cfg["ZOTERO_COLLECTION"]
    for c in paged(cfg, "/collections"):
        if c["data"]["name"] == name:
            return c["key"]
    die(f"collection '{name}' not found in library {cfg['ZOTERO_USER_ID']}")


def citation_key(data, taken):
    creators = data.get("creators", [])
    authors = [c for c in creators if c.get("creatorType") == "author"] or creators
    surname = authors[0].get("lastName") or authors[0].get("name", "Unknown") if authors else "Unknown"
    surname = re.sub(r"[^A-Za-z]", "", surname) or "Unknown"
    m = re.search(r"\b(19|20)\d{2}\b", data.get("date", ""))
    year = m.group(0) if m else "NoYear"
    keyword = "Paper"
    for w in re.findall(r"[A-Za-z0-9]+", data.get("title", "")):
        if w.lower() not in STOPWORDS:
            keyword = w[0].upper() + w[1:]
            break
    key = f"{surname}{year}_{keyword}"
    suffix = "b"
    while key in taken:
        key = f"{surname}{year}{suffix}_{keyword}"
        suffix = chr(ord(suffix) + 1)
    return key, year


def pdf_attachment(cfg, item_key):
    for child in paged(cfg, f"/items/{item_key}/children"):
        d = child["data"]
        if d.get("itemType") == "attachment" and d.get("contentType") == "application/pdf":
            return child["key"]
    return None


def main():
    cfg = load_config()
    coll = find_collection(cfg)
    state = json.loads(STATE_FILE.read_text()) if STATE_FILE.exists() else {}
    taken = {v["citation_key"] for v in state.values()}
    new, skipped, no_pdf = 0, 0, []

    for item in paged(cfg, f"/collections/{coll}/items/top"):
        data = item["data"]
        if data.get("itemType") in ("attachment", "note"):
            continue
        if item["key"] in state:
            skipped += 1
            continue
        att = pdf_attachment(cfg, item["key"])
        if not att:
            no_pdf.append(data.get("title", item["key"]))
            continue
        key, year = citation_key(data, taken)
        pdf = api_get(cfg, f"/items/{att}/file", raw=True)
        CORPUS.mkdir(exist_ok=True)
        (CORPUS / f"{key}.pdf").write_bytes(pdf)
        sidecar = {
            "citation_key": key,
            "title": data.get("title", ""),
            "creators": data.get("creators", []),
            "year": year,
            "venue": data.get("publicationTitle") or data.get("conferenceName")
                     or data.get("proceedingsTitle") or "",
            "doi": data.get("DOI", ""),
            "url": data.get("url", ""),
            "zotero_item_key": item["key"],
        }
        (CORPUS / f"{key}.zotero.json").write_text(json.dumps(sidecar, indent=2) + "\n")
        state[item["key"]] = {"citation_key": key, "status": "downloaded"}
        taken.add(key)
        new += 1
        print(f"downloaded: {key}.pdf")

    STATE_FILE.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n")
    print(f"\n{new} new, {skipped} already known")
    for title in no_pdf:
        print(f"no PDF attachment (not downloaded): {title}")


if __name__ == "__main__":
    main()
