from openai import OpenAI
from config.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)


def create_plan(goal):

    system_prompt = """
You are an AI planning assistant.

Break the goal into numbered steps.

Example:

Goal: Research AI agent frameworks

Plan:
1. Search frameworks
2. Gather features
3. Compare frameworks
4. Summarize
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": goal}
        ]
    )

    return response.choices[0].message.content