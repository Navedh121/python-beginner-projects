# Python CLI Projects

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=flat)

Three command-line utilities built while learning Python and API integration. Each one solves a small real problem.

---

## Projects

| Script | What it does | API Used |
|---|---|---|
| `weather.py` | Fetches live weather for any city | OpenWeatherMap |
| `quote.py` | Prints 1–5 random quotes on demand | ZenQuotes (free, no key needed) |
| `organiser.py` | Sorts a messy folder into subfolders by file type | None (filesystem only) |

---

## What I Learned Here

- How HTTP GET requests work (sending params, reading JSON responses)
- Parsing API responses and pulling out the data you need
- Storing secrets in `.env` files instead of hardcoding them
- Basic file I/O with `os` and `shutil`

These were the first projects where "write some Python" turned into "build something that talks to the internet."

---

## How to Run

```bash
# Install dependencies
pip install -r requirements.txt

# Set your OpenWeatherMap API key
cp .env.example .env
# Edit .env and add: OPENWEATHER_API_KEY=your_key_here

# Run any script
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
