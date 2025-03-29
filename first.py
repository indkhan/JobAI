from browser_use import Agent, Browser, BrowserConfig
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI

import asyncio

load_dotenv()


llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# gemini-2.5-pro-exp-03-25,gemini-2.0-flash-lite,gemini-2.0-flash


browser = Browser(
    config=BrowserConfig(
        # Specify the path to your Chrome executable
        chrome_instance_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        # For Linux, typically: '/usr/bin/google-chrome'
    )
)


async def main():
    agent = Agent(
        task="go to youtube and search for 'python programming'",
        llm=llm,
        save_conversation_path="logs/conversation",
        browser=browser,
    )
    result = await agent.run()
    print(result)
    input("Press Enter to close the browser...")
    await browser.close()


asyncio.run(main())
