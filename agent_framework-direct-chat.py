import asyncio
import dotenv
import os
from agent_framework import ChatAgent
from agent_framework.openai import OpenAIChatClient

dotenv.load_dotenv()
url = os.getenv("API_URL")
model = os.getenv("MODEL_FREE_8B")
api_key = os.getenv('API_KEY')

import asyncio
from agent_framework import ChatMessage
from agent_framework.openai import OpenAIChatClient

async def main():
    client = OpenAIChatClient(
        base_url=os.environ.get("API_URL"),
        api_key=os.environ.get("API_KEY"), 
        model_id=os.environ.get("MODEL_FREE_8B")
    )

    messages = [
        ChatMessage(role="system", text="You are a helpful assistant."),
        ChatMessage(role="user", text="Write a haiku about Agent Framework.")
    ]

    response = await client.get_response(messages)
    print(response.messages[0].text)

    """
    Output:

    Agents work in sync,
    Framework threads through each task—
    Code sparks collaboration.
    """

asyncio.run(main())