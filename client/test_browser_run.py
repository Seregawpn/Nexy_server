
import asyncio
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent
from dotenv import load_dotenv

# Initialize a simple test
async def main():
    print("🚀 Starting Browser Use Test...")
    
    # We need an API key for the agent to work. 
    # I will try to read it from the user's config or env, but for a quick test 
    # checking if browser launches is usually enough. 
    # However, 'Agent' requires an LLM.
    
    # Let's check if we can just launch the browser directly via Playwright 
    # to verify the binary exists and works, avoiding LLM key dependency for this purely "browser" test.
    
    print("Checking Playwright Browser Launch...")
    from playwright.async_api import async_playwright
    
    async with async_playwright() as p:
        try:
            browser = await p.chromium.launch(headless=False)
            print("✅ Browser launched successfully!")
            
            page = await browser.new_page()
            await page.goto("https://www.google.com")
            title = await page.title()
            print(f"✅ Page loaded. Title: {title}")
            
            await asyncio.sleep(2) # Keep it open briefly
            await browser.close()
            print("✅ Browser closed.")
            print("SUCCESS: Browser automation infrastructure is working.")
        except Exception as e:
            print(f"❌ Failed to launch browser: {e}")

if __name__ == "__main__":
    asyncio.run(main())
