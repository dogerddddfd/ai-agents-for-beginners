import asyncio
import dotenv
import os
from agent_framework import ChatAgent
from agent_framework.openai import OpenAIChatClient

dotenv.load_dotenv()
url = os.getenv("API_URL")
model = os.getenv("MODEL_FREE_8B")
api_key = os.getenv('API_KEY')

async def main():
    agent = ChatAgent(
        chat_client=OpenAIChatClient(
            base_url=os.environ.get("API_URL"),
            api_key=os.environ.get("API_KEY"), 
            model_id=os.environ.get("MODEL_FREE_8B")
        ),
        instructions="""
        1) A robot may not injure a human being...
        2) A robot must obey orders given it by human beings...
        3) A robot must protect its own existence...

        Give me the TLDR in exactly 5 words.
        """
    )

    result = await agent.run("Summarize the Three Laws of Robotics")
    print(result)

asyncio.run(main())
# Output: Protect humans, obey, self-preserve, prioritized.