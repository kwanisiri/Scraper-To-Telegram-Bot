# LeadScraper Agent

This is a modular, AI-powered lead generation bot for scraping builder job posts and auto-notifying high-value opportunities.


# LeadScraper FastAPI App

A modern, async Python application for scraping leads from websites, scoring them, and optionally sending notifications to Telegram. Built with FastAPI, Playwright, Pydantic, and python-telegram-bot.

---

## Features

- **Web Scraping:** Uses Playwright to extract leads (e.g., quotes/authors) from target websites.
- **Lead Scoring:** Custom scoring logic for each lead.
- **REST API:** FastAPI endpoints for triggering scraping and retrieving results.
- **Telegram Notifications:** Sends new leads to a Telegram chat (optional, configurable).
- **Configurable:** Uses a `.env` file and Pydantic settings for easy configuration.

---

## Setup

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd drop
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install fastapi uvicorn playwright pydantic-settings python-telegram-bot
playwright install
```

### 4. Configure environment variables

Create a `.env` file in the project root with:

```
ENABLE_TELEGRAM=True
TELEGRAM_TOKEN=your-telegram-bot-token
CHAT_ID=your-chat-id
```

Set `ENABLE_TELEGRAM=False` if you do not want Telegram notifications.

---

## Running the App

```bash
uvicorn app.main:app --reload
```

- Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for the interactive API docs.

---

## Usage

- **GET /**  
  Health check endpoint.

- **POST /scrape**  
  Triggers scraping, scoring, and (if enabled) Telegram notification. Returns a list of leads as JSON.

**Quick Example:**
```bash
curl -X POST http://127.0.0.1:8000/scrape
```

---

## Data Model

The `Lead` model (in `models.py`) defines the structure of a lead:

```python
from pydantic import BaseModel

class Lead(BaseModel):
    name: str
    url: str
    score: float
```

---

## Project Structure

```
drop/
├── app/
│   ├── config.py        # Pydantic settings and config loader
│   ├── main.py          # FastAPI app and endpoints
│   ├── models.py        # Lead data model
│   ├── notify.py        # Telegram notification logic
│   └── scraper.py       # Scraping and scoring logic
├── .env                 # Environment variables (not committed)
└── ...
```

---

## Extending

- Add more scraping targets in `scraper.py`.
- Enhance scoring logic.
- Add more notification channels (email, Slack, etc.).
- Integrate with a database or CRM.

---

## Security: Prevent Committing `.env`

**Never commit your `.env` file to public repositories!**  
It contains sensitive credentials.

**To ensure this:**

1. Add `.env` to your `.gitignore` file in the project root:
    ```
    # .gitignore
    .env
    ```
2. If you already committed `.env`, remove it from git history:
    ```bash
    git rm --cached .env
    git commit -m "Remove .env from version control"
    ```

---

## License

MIT (or your preferred license)

---

## Credits

- [FastAPI](https://fastapi.tiangolo.com/)
- [Playwright](https://playwright.dev/python/)
- [Pydantic](https://docs.pydantic.dev/)
- [python-telegram-bot](https://python-telegram-bot.org/)

---

*Happy scraping!*