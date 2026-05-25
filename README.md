# Python CLI Projects

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=flat)

Where I started. Three command-line utilities built while learning Python and real API integration. Each one taught me something specific before I moved on to AI web apps and automation bots.

---

## Projects

| Script | What it does | What it taught me |
|---|---|---|
| `weather.py` | Live weather for any city | HTTP GET requests, JSON parsing, `.env` secrets |
| `quote.py` | Prints 1-5 random quotes on demand | API patterns (request → JSON → extract) |
| `organiser.py` | Sorts a folder into subfolders by file type | File I/O with `os` and `shutil` |

---

## How to Run

```bash
pip install -r requirements.txt

# For weather.py — add your free OpenWeatherMap key
cp .env.example .env
# Edit .env: OPENWEATHER_API_KEY=your_key_here

python weather.py
python quote.py
python organiser.py
```

---

## Repo Structure

```
python-projects/
├── weather.py       # Weather lookup CLI
├── quote.py         # Quote of the day bot
├── organiser.py     # File sorter by type
├── requirements.txt
└── .env.example
```

---

> Part of a learning series: CLI tools → [AI web apps](https://github.com/Navedh121/ai-projects) → [Automation bots](https://github.com/Navedh121/python-automation-bots)
