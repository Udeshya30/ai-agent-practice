from openai import OpenAI
from config import OPENAI_API_KEY
from tools import search_web
from planner import create_plan

client = OpenAI(api_key=OPENAI_API_KEY)


def run_agent(user_input):

    # Step 1 — Create plan
    plan = create_plan(user_input)

    print("\nGenerated Plan:\n")
    print(plan)

    system_prompt = """
You are an AI research agent.

You can use the tool:

search_web(query)

Follow this format:

THOUGHT: reasoning
ACTION: search_web
INPUT: query

When you receive results you will see:

OBSERVATION: tool output

When finished respond:

FINAL: answer
"""

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"Goal: {user_input}\n\nPlan:\n{plan}"}
    ]

    while True:

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )

        message = response.choices[0].message.content

        print("\nAgent reasoning:\n")
        print(message)

        messages.append({"role": "assistant", "content": message})

        # Handle tool action
        if "ACTION:" in message:

            action = message.split("ACTION:")[1].split("\n")[0].strip()

            if action == "search_web":

                query = message.split("INPUT:")[1].strip()

                print("\nExecuting search tool...\n")

                results = search_web(query)

                observation = f"OBSERVATION: {results}"

                messages.append({"role": "user", "content": observation})

        # Finish
        if "FINAL:" in message:

            final_answer = message.split("FINAL:")[1].strip()
            return final_answer


def main():

    print("\nAI Agent Started")
    print("Type 'exit' to quit\n")

    while True:

        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        answer = run_agent(user_input)

        print("\nAgent:", answer)
        print()


if __name__ == "__main__":
    main()