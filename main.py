from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent      # FIXED IMPORT
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

def main():
    # Initialize the language model
    model = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    tools = []

    # Create the ReAct agent
    agent = create_react_agent(model=model, tools=tools)

    print("Welcome to the AI Agent. Type 'exit' to quit.")
    print("You can ask questions or give commands.")

    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting the AI Agent. Goodbye!")
            break

        print("\nAssistant:", end=" ")
        
        for chunk in agent.stream({"messages": [HumanMessage(content=user_input)]}):
            content = chunk.get("agent", {}).get("message", "")
            if content:
                print(content, end="")

if __name__ == "__main__":
    main()
