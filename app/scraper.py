from typing import List
from app.models import Lead
from playwright.async_api import async_playwright
from app.scoring import score_lead

async def scrape_site() -> List[Lead]:
    leads = []  # Initialize an empty list to store Lead objects

    try:
        async with async_playwright() as p:  # Start Playwright in async context
            browser = await p.chromium.launch(headless=True)  # Launch Chromium browser in headless mode
            page = await browser.new_page()  # Open a new browser page/tab
            await page.goto("https://quotes.toscrape.com")  # Navigate to the target website

            quotes = await page.query_selector_all(".quote")  # Select all elements with class 'quote'

            for quote in quotes:  # Loop through each quote element
                try:
                    text_el = await quote.query_selector(".text")  # Find the element containing the quote text
                    author_el = await quote.query_selector(".author")  # Find the element containing the author
                    text = await text_el.text_content() if text_el else ""  # Get the text content or empty string
                    author = await author_el.text_content() if author_el else ""  # Get the author or empty string
                    leads.append(
                        Lead(
                            name=author.strip() if author else "",  # Strip whitespace if author exists, else empty
                            url="https://quotes.toscrape.com",  # Set the source URL
                            score=0  # Set a default score of 0
                        )
                    )
                except Exception as inner_err:
                    print("⚠️ Error in quote parsing:", inner_err)  # Print error if quote parsing fails
            await browser.close()  # Close the browser after scraping

    except Exception as e:
        print("🔥 Main scrape error:", e)  # Print error if the main scraping process fails

    # Commented out Telegram logic to avoid errors if Telegram is not set up
    def send_leads_to_telegram(leads):
        # Placeholder function: implement Telegram sending logic here
        print(f"Sending {len(leads)} leads to Telegram (placeholder)")

    try:
        send_leads_to_telegram(leads)
    except Exception as telegram_err:
        print("Telegram error:", telegram_err)

    return leads  # Return the list of Lead objects

async def scrape_and_score():
    leads = await scrape_site()  # Scrape leads from the target website
    for lead in leads:
        lead.score = score_lead(lead)  # Score each lead using custom logic
    return leads

