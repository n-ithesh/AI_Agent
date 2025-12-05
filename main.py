from email.mime import message
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

def main():
    # Initialize the language model
    model = ChatOpenAI(temperature=0)

    tools = []

    # Create the ReAct agent
    agent = create_react_agent(model, tools)

    print("Welcome to the AI Agent. Type 'exit' to quit.")
    print("You can ask questions or give commands.")

    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() == 'exit' or user_input.lower() == 'quit':
            print("Exiting the AI Agent. Goodbye!")
            break
        print("\nAssistant:", end=" ")
        for chunk in agent.stream(
            {"messages": [HumanMessage(content=user_input)]}
        ):
            if "agent" in chunk and  "message" in chunk["agent"]:
               from message in chunk["agent"]["message"]
               print(message, end="")