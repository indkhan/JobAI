from browser_use import Agent, Browser, BrowserConfig, Controller, ActionResult
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI

import asyncio

from pydantic import BaseModel


load_dotenv()

class Post(BaseModel):
    post_title:str
    post_url:str
    num_comments: int
    hours_since_post: int

class Posts(BaseModel):
    posts:List[Post]






llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# gemini-2.5-pro-exp-03-25,gemini-2.0-flash-lite,gemini-2.0-flash


# Initialize the controller
controller = Controller(output_model=Posts)



browser = Browser(
    config=BrowserConfig(
        # Specify the path to your Chrome executable
        chrome_instance_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        # For Linux, typically: '/usr/bin/google-chrome'
    )
)

initial_actions = [
    {'open_tab':{'url':'https://www.linkedin.com/jobs/'}}
        ]

async def main():
    agent = Agent(
            task="Find a job on linkedin and search for job related to Software development and print the job description",
        llm=llm,
        save_conversation_path="logs/conversation",
        browser=browser,
        initial_actions = initial_actions,
        controller=controller,
    )
    results = await agent.run()
    result = results.final_result()
    if result:
        parsed: Posts = Posts.model_validate_json(result)
        for post in parsed.posts:
            print('\n----------------------')
            print(f'Title:              {post.post_title}')
            print(f'URL:                {post.post_url}')
            print(f'COmments:           {post.num_comments}')
            print(f'Hours since post:   {post.hours_since_post}')
        else:
            print('No results')



if __name__ == '__main__':
    asyncio.run(main())
