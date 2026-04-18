from config.settings import settings
from langchain.agents import create_agent
from langchain_ollama import ChatOllama

def get_phase_goal(phase_name: str) -> str:
    """Return the learning goal for a named phase."""
    goals = {
        "phase 1": "Set up a clean Python workspace and build one simple LangChain agent that can use a tool."
    }
    return goals.get(phase_name.lower().strip(), "Unknown phase")

model = ChatOllama(
    model=settings.ollama_model,
    base_url=settings.ollama_base_url,
)

agent = create_agent(
    model=model,
    tools=[get_phase_goal],
    system_prompt="You are a beginner-friendly AI tutor. Use tools when helpful."
)

print("Phase 1 Agent Chat")
print("Ask a question about Phase 1.")
print("Type 'exit' to quit.\n")

while True:
    user_question = input("Your question: ").strip()

    if user_question.lower() in {"exit", "quit"}:
        print("\nGoodbye!")
        break

    if not user_question:
        print("\nPlease enter a question.\n")
        continue

    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": user_question
                }
            ]
        }
    )

    print("\nAgent response:")
    print(result["messages"][-1].content)
    print()