# Kindle Clippings → Notion → Daily Emails

Personal knowledge management system that resurfaces Kindle highlights automatically.

## Problem
500+ book highlights buried in Kindle app, never revisited.

## Solution
- **Python script**: parses `My Clippings.txt` → structured CSV
- **Notion database**: imports highlights with metadata (book, author, date)
- **Make.com**: sends 1 random highlight via email every morning

## Files
- `parse_clippings.py`: main script
- `20240505_kindle_clippings_converter.html`: sample output for testing

## Stack
- Python 3.x
- Notion API
- Make.com (automation)
- Raycast AI (vibe code)

Note: This is a personal tool built in 3 days. Code is functional but not production-ready.
