import re
from openai import OpenAI
from config.config import OPENAI_API_KEY
from tools.registry import TOOL_REGISTRY

client = OpenAI(api_key=OPENAI_API_KEY)


def execute(goal, plan, memory):

    system_prompt = """
You are an AI research agent.

You can use tools:

search_web(query)
calculator(expression)

When using a tool you MUST follow EXACT format:

THOUGHT: reasoning
ACTION: tool_name
INPUT: tool input

Example:

THOUGHT: I should search for AI frameworks
ACTION: search_web
INPUT: AI agent frameworks

When finished respond:

FINAL: answer
"""

    messages = [
        {"role": "system", "content": system_prompt}
    ]

    messages.extend(memory.get())

    messages.append({
        "role": "user",
        "content": f"Goal: {goal}\n\nPlan:\n{plan}"
    })

    while True:

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )

        message = response.choices[0].message.content

        print("\nAgent reasoning:\n", message)

        messages.append({"role": "assistant", "content": message})
        memory.add("assistant", message)

        if "ACTION:" in message:


            action_line = message.split("ACTION:")[1].split("\n")[0].strip()

            # Case 1: search_web(query)
            match = re.search(r'(\w+)\("(.*)"\)', action_line)

            if match:
                action = match.group(1)
                query = match.group(2)

            # Case 2: normal format
            else:
                action = action_line

                if "INPUT:" in message:
                    query = message.split("INPUT:")[1].split("\n")[0].strip()
                else:
                    query = None

            if action == "None":
                continue
                
            if action in TOOL_REGISTRY:

                tool = TOOL_REGISTRY[action]

                print(f"\n🔧 Running tool: {action}")

                result = tool(query)

                observation = f"OBSERVATION: {result}"

                messages.append({"role": "user", "content": observation})
                memory.add("user", observation)

        if "FINAL:" in message:

            return message.split("FINAL:")[1].strip()