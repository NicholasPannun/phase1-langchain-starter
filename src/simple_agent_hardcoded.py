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

result = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "What is the goal of Phase 1? Use your tool if needed."
            }
        ]
    }
)

print("\nAgent response:")
print(result["messages"][-1].content)