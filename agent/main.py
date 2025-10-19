from pydantic_ai import Agent
from pydantic_ai.models.google import GoogleModel
from pydantic_ai.providers.google import GoogleProvider
import os 
from dotenv import load_dotenv

load_dotenv()

provider = GoogleProvider(api_key=os.getenv("GOOGLE_API_KEY"))
model = GoogleModel('gemini-2.5-flash', provider=provider)
agent = Agent(model)

async def main():
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            break
        response = await agent.run(user_input)
        print(f"Agent: {response.output}")


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
    
