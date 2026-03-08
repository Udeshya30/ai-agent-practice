from agent.planner import create_plan
from agent.executor import execute
from memory.memory import AgentMemory


memory = AgentMemory()


def run_agent(user_input):

    memory.add("user", user_input)

    print("\nCreating plan...")

    plan = create_plan(user_input)

    print("\nPlan:\n", plan)

    result = execute(user_input, plan, memory)

    return result