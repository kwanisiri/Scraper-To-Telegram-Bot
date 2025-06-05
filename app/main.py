from fastapi import FastAPI
from app.scraper import scrape_and_score
from app.models import Lead
from app.config import settings
from app.notify import notify_telegram

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "LeadScraper API is running"}

@app.post("/scrape")
async def run_scraper():
    leads = await scrape_and_score()
    if settings.enable_telegram:
        for lead in leads:
            try:
                await notify_telegram(lead)
            except Exception as e:
                print("Telegram error:", e)
    return {"status": "done", "leads": [lead.dict() for lead in leads]}
