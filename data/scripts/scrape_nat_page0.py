#!/usr/bin/env python3
# scripts/scrape_nat.py
"""
Scrape NCO (NAT) occupations from DGE site across all pages.

Output:
- raw/nat_page_{page:03d}.csv  → per-page CSV
- raw/nat_all.csv              → combined CSV
- raw/nat_all.json             → combined JSON
"""

import time, csv, json, requests
from bs4 import BeautifulSoup
from pathlib import Path
from tqdm import trange

BASE = "https://dge.gov.in/dge/nat?field_group_nat_target_id=All&field_occupation_nat_code_value=&page={page}"
RAW = Path("raw"); RAW.mkdir(parents=True, exist_ok=True)

HEADERS = {"User-Agent": "CNOC-DataBot/1.0 (contact: your-team@org)"}


def parse_all_tables(soup):
    """Parse all tables on the page; each occupation family is its own table"""
    rows = []
    tables = soup.find_all("table")
    for table in tables:
        for tr in table.find_all("tr"):
            cells = [td.get_text(strip=True) for td in tr.find_all(["th", "td"])]
            if len(cells) >= 8 and cells[0].isdigit():
                rows.append({
                    "sno": cells[0],
                    "title": cells[1],
                    "nco_2015": cells[2],
                    "nco_2004": cells[3],
                    "division": cells[4],
                    "sub_division": cells[5],
                    "group": cells[6],
                    "family": cells[7],
                })
    return rows


def scrape_page(p):
    """Download and parse a single page"""
    url = BASE.format(page=p)
    r = requests.get(url, headers=HEADERS, timeout=30)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "lxml")
    return parse_all_tables(soup)


def main(max_pages=300):
    all_rows, seen = [], set()

    for p in trange(max_pages, desc="Scraping pages"):
        rows = scrape_page(p)
        if not rows:
            print(f"\nNo rows found on page {p}, stopping.")
            break

        # Deduplicate by (nco_2015, title)
        new = [r for r in rows if (r["nco_2015"], r["title"]) not in seen]
        if not new:
            print(f"\nAll rows on page {p} were duplicates, stopping.")
            break

        for r in new:
            seen.add((r["nco_2015"], r["title"]))
        all_rows.extend(new)

        # Save page CSV
        page_csv = RAW / f"nat_page_{p:03d}.csv"
        with page_csv.open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(new[0].keys()))
            w.writeheader()
            w.writerows(new)

        time.sleep(0.8)  # polite crawling

    # Save combined outputs
    if all_rows:
        keys = list(all_rows[0].keys())
        with (RAW / "nat_all.csv").open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=keys)
            w.writeheader()
            w.writerows(all_rows)

        (RAW / "nat_all.json").write_text(
            json.dumps(all_rows, ensure_ascii=False, indent=2),
            encoding="utf-8"
        )
        print(f"\n✅ Done! Saved {len(all_rows)} rows.")


if __name__ == "__main__":
    main()
