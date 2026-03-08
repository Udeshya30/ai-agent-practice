from openai import OpenAI
from ai_agent_01.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)


def create_plan(goal):

    system_prompt = """
You are an AI planning assistant.

Your job is to break a goal into clear numbered steps.

Example:

Goal: Research AI agent frameworks

Plan:
1. Search top AI agent frameworks
2. Collect key features
3. Compare frameworks
4. Produce final summary
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": goal}
        ]
    )

    plan = response.choices[0].message.content
    return plan