# README.md


# 🧠 AI Research Agent (Planner + Executor Architecture)

This project implements a **simple AI Research Agent** that can:

- Understand a **user goal**
- Create a **plan to achieve the goal**
- Use **tools (web search)** to gather information
- Perform **multi-step reasoning**
- Produce a **final summarized answer**

The agent follows a **Planner → Executor → Tool → Observation loop**, which is a simplified version of architectures used in modern AI systems like:

- AutoGPT
- CrewAI
- OpenAI Deep Research
- Microsoft AutoGen

---

# 🚀 Project Overview

This project demonstrates how to build a **basic Agentic AI system from scratch using Python and OpenAI APIs**.

Instead of a normal chatbot:

```

User → LLM → Answer

```

This system behaves like an **AI agent**:

```

User Goal
↓
Planner (LLM)
↓
Executor Agent
↓
Tools
↓
Observation
↓
Final Answer

```

---

# 🧩 Architecture

```

```
            USER
              │
              ▼
       ┌─────────────┐
       │   PLANNER   │
       │ (planner.py)│
       └──────┬──────┘
              │
              ▼
      ┌───────────────┐
      │ EXECUTOR AGENT│
      │   (agent.py)  │
      └──────┬────────┘
             │
             ▼
         ┌─────────┐
         │  TOOLS  │
         │tools.py │
         └────┬────┘
              │
         Web Search
              │
              ▼
         OBSERVATION
              │
              ▼
         FINAL ANSWER
```

```

---

# 📂 Project Structure

```

ai-agent
│
├── agent.py       # Main agent executor
├── planner.py     # Planning module
├── tools.py       # External tools (web search)
├── config.py      # Environment configuration
├── requirements.txt
└── .env

```

---

# ⚙️ Installation

### 1. Clone the project

```

git clone <repo-url>
cd ai-agent

```

---

### 2. Create virtual environment

```

python -m venv .venv

```

Activate:

Windows:

```

.venv\Scripts\activate

```

Mac/Linux:

```

source .venv/bin/activate

```

---

### 3. Install dependencies

```

pip install -r requirements.txt

```

Dependencies:

```

openai
python-dotenv
ddgs

```

---

### 4. Add OpenAI API Key

Create `.env` file:

```

OPENAI_API_KEY=your_api_key_here

```

---

# ▶️ Running the Agent

Run:

```

python agent.py

```

Example prompt:

```

Research AI agent frameworks and compare them

```

Example output:

```

🧠 Generated Plan:

1. Identify AI agent frameworks
2. Gather key features
3. Compare frameworks
4. Produce summary

THOUGHT: I should search for frameworks
ACTION: search_web
INPUT: AI agent frameworks

```

---

# 🧠 Core Concepts Implemented

This project implements several **key concepts of Agentic AI**.

---

# 1️⃣ Planner

File:

```

planner.py

```

The planner converts a **goal into steps**.

Example:

```

Goal:
Research AI agent frameworks

Generated Plan:

1. Search frameworks
2. Collect features
3. Compare them
4. Produce summary

```

Code reference: :contentReference[oaicite:0]{index=0}

Planner uses the **LLM as a planning engine**.

```

User Goal
↓
LLM generates steps
↓
Executor follows plan

```

---

# 2️⃣ Executor Agent

File:

```

agent.py

```

This is the **core agent loop**.

Code reference: :contentReference[oaicite:1]{index=1}

The agent follows a **ReAct pattern**:

```

THOUGHT
ACTION
INPUT
OBSERVATION
FINAL

```

Example reasoning loop:

```

THOUGHT: I need to search for AI agent frameworks
ACTION: search_web
INPUT: AI agent frameworks

OBSERVATION: search results

THOUGHT: I now have enough information

FINAL: summary

```

This pattern is used in many modern agent systems.

---

# 3️⃣ Tools System

File:

```

tools.py

```

Code reference: :contentReference[oaicite:2]{index=2}

Tools allow the agent to **interact with the external world**.

Current tool implemented:

```

search_web(query)

```

This uses **DuckDuckGo Search API (ddgs)**.

Example tool output:

```

[
{title: "...", link: "...", snippet: "..."},
{title: "...", link: "...", snippet: "..."}
]

```

The agent receives this as an **OBSERVATION**.

---

# 4️⃣ Environment Configuration

File:

```

config.py

```

Code reference: :contentReference[oaicite:3]{index=3}

Purpose:

- Load environment variables
- Secure API keys

Example:

```

OPENAI_API_KEY=xxxx

```

---

# 🔁 Agent Execution Flow

Full runtime flow:

```

User Input
↓
Planner generates steps
↓
Executor agent starts reasoning
↓
Agent decides to use tool
↓
Tool executes
↓
Results returned
↓
Agent analyzes results
↓
Final answer produced

```

---

# 🧠 Reasoning Pattern (ReAct)

The agent uses the **ReAct reasoning pattern**.

ReAct = **Reason + Act**

```

THOUGHT → reasoning
ACTION → tool call
INPUT → tool input
OBSERVATION → tool output
FINAL → answer

```

This pattern is widely used in:

- LangChain Agents
- AutoGPT
- CrewAI
- AutoGen

---

# 🧩 Example Interaction

User:

```

Research AI agent frameworks and compare them

```

Agent:

```

Plan:
1 Identify frameworks
2 Gather details
3 Compare frameworks
4 Summarize

```

Agent reasoning:

```

THOUGHT: I need to search for frameworks
ACTION: search_web
INPUT: AI agent frameworks

```

Tool runs:

```

search_web()

```

Observation returned:

```

OBSERVATION: results

```

Agent final output:

```

FINAL: framework comparison

```

---

# ⚠️ Current Limitations

This is a **learning implementation**, so it lacks some advanced capabilities.

Missing features:

- Memory system
- Vector database
- Multiple tools
- Autonomous loop
- Multi-agent collaboration

---

# 🚀 Future Improvements

Possible upgrades:

### Memory System

Store previous results.

```

Conversation history
Research notes
Knowledge storage

```

---

### Vector Database

Add:

```

FAISS
Chroma
Weaviate

```

For knowledge retrieval.

---

### More Tools

Example tools:

```

calculator
python code executor
database query
file reader
API tools

```

---

### Multi-Agent Architecture

Example:

```

Manager Agent
Research Agent
Writer Agent

```

Similar to **CrewAI**.

---

# 📚 Concepts Demonstrated

This project demonstrates:

- Agentic AI
- Planner-Executor Architecture
- ReAct Pattern
- Tool Use
- LLM Reasoning
- Autonomous Task Execution

---

# 🎯 Learning Outcome

By building this project you learn:

- How AI agents are structured
- How LLMs reason and call tools
- How to implement planning
- How modern agent frameworks work internally

---

# 📖 References

Concepts inspired by:

- OpenAI Agent research
- ReAct paper
- AutoGPT architecture
- CrewAI agent systems
- LangChain agents
```

---

# Mentor Tip

If you want, I can also help you add **advanced diagrams like real agent architecture diagrams**, including:

* **ReAct reasoning diagram**
* **Planner-Executor architecture**
* **Agent lifecycle flow**
* **Multi-agent architecture**

Those will make your README look **extremely professional (GitHub showcase level)**.
