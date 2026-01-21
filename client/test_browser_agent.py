
import asyncio
import os
# Use the internal wrapper from browser_use which likely adds the required 'provider' attribute
from browser_use import Agent, Browser, ChatGoogle

# Helper to test full agent flow
async def main():
    print("🚀 Starting Full Browser Agent Test...")
    
    # Set API Key explicitly from config
    os.environ["GOOGLE_API_KEY"] = "AIzaSyBB6iKD1oeW_GdidzhBgx68s-OsCRDpJiA"
    
    try:
        # Initialize LLM using browser-use wrapper
        llm = ChatGoogle(
            model="gemini-2.0-flash-exp",
            temperature=0,
            # google_api_key might represent api_key in this wrapper
            api_key=os.environ["GOOGLE_API_KEY"]
        )
        
        # Initialize Browser
        browser = Browser()
        
        # Initialize Agent
        task = "Go to Google.com and search for 'current bitcoin price'. Return the price you find."
        print(f"🎯 Task: {task}")
        
        agent = Agent(
            task=task,
            llm=llm,
            browser=browser
        )
        
        print("🤖 running agent...")
        history = await agent.run()
        
        print("✅ Agent run complete!")
        # Print just the final result if possible to avoid massive output
        if history and hasattr(history, 'final_result'):
             print("📊 Final Result:", history.final_result())
        else:
             print("📊 Result History:", history)
        
        # Clean shutdown
        await browser.close()
        
    except Exception as e:
        print(f"❌ Test Failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main())
