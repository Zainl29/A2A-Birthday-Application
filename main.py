import uvicorn
from a2a.server.apps import A2AStarletteApplication
from a2a.server.request_handlers import DefaultRequestHandler
from a2a.server.tasks import InMemoryTaskStore
from a2a.types import AgentCapabilities, AgentCard, AgentSkill
from agent_executor import BirthdayAgentExecutor


def main():
    skill = AgentSkill(
        id="birthday_retrieval",
        name="Birthday Retrieval",
        description="Returns the date of birth for a given person",
        tags=["birthday", "date of birth", "dob"],
        examples=["What is Zain's date of birth?", "When was Zain born?"],
    )

    agent_card = AgentCard(
        name="Birthday Agent",
        description="An agent that returns date of birth information",
        url="http://localhost:9999/",
        defaultInputModes=["text"],
        defaultOutputModes=["text"],
        skills=[skill],
        version="1.0.0",
        capabilities=AgentCapabilities(),
    )

    request_handler = DefaultRequestHandler(
        agent_executor=BirthdayAgentExecutor(),
        task_store=InMemoryTaskStore(),
    )

    server = A2AStarletteApplication(
        http_handler=request_handler,
        agent_card=agent_card,
    )

    uvicorn.run(server.build(), host="127.0.0.1", port=9999)


if __name__ == "__main__":
    main()
