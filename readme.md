# 🧠 AI Research Agent (Planner–Executor Architecture)

This project implements a **modular AI Agent system** capable of:

* Understanding a **user goal**
* Generating a **plan to solve the goal**
* Using **tools (web search, calculator)** to gather information
* Running a **ReAct reasoning loop**
* Producing a **final response**
* Exposing the agent through both **CLI and API**

The architecture demonstrates how **modern Agentic AI systems work internally**.

Inspired by systems such as:

* AutoGPT
* CrewAI
* LangGraph
* Microsoft AutoGen
* OpenAI Deep Research Agents

---

# 🚀 Features

* Planner–Executor agent architecture
* Tool registry system
* Web search capability
* Calculator tool
* Conversation memory
* FastAPI API interface
* Terminal interaction mode

---

# 🧩 Architecture

The agent follows a **Planner → Executor → Tool → Observation loop**.

```
User / API
   │
   ▼
Controller
   │
   ▼
Planner
   │
   ▼
Executor (ReAct Loop)
   │
   ▼
Tool Registry
   │
   ▼
Tools
   │
   ▼
Observation
   │
   ▼
Memory
   │
   ▼
Final Answer
```

---

# ⚙️ Project Structure

```
ai_agent/
│
├── api/
│   └── api.py
│
├── agent/
│   ├── controller.py
│   ├── executor.py
│   └── planner.py
│
├── tools/
│   ├── search_tool.py
│   ├── calculator_tool.py
│   └── registry.py
│
├── memory/
│   └── memory.py
│
├── config/
│   └── config.py
│
├── main.py
├── requirements.txt
└── .env
```

---

# 🧠 Agent Workflow

The agent operates using a **ReAct reasoning pattern**.

```
THOUGHT → reasoning
ACTION → tool call
INPUT → tool parameters
OBSERVATION → tool result
FINAL → response
```

Example:

```
THOUGHT: I need to search for AI frameworks
ACTION: search_web
INPUT: AI agent frameworks
```

---

# 🔧 Tools Implemented

### Web Search Tool

```
search_web(query)
```

Uses DuckDuckGo search to gather real-time information.

---

### Calculator Tool

```
calculator(expression)
```

Performs arithmetic operations requested by the agent.

---

# 🧠 Planner

The planner converts a **user goal into task steps**.

Example:

```
Goal:
Research AI agent frameworks

Plan:
1 Identify frameworks
2 Gather key features
3 Compare frameworks
4 Produce summary
```

---

# 🔁 Executor Loop

The executor runs a reasoning loop:

```
Goal
 ↓
Plan
 ↓
THINK
 ↓
ACT
 ↓
OBSERVE
 ↓
REPEAT
```

---

# ▶️ Running the Agent

## 1. Install dependencies

```
pip install -r requirements.txt
```

---

## 2. Add OpenAI API key

Create `.env` file:

```
OPENAI_API_KEY=your_api_key_here
```

---

## 3. Run CLI Agent

```
python main.py
```

Example query:

```
Research AI agent frameworks
```

---

## 4. Run API Server

```
uvicorn ai_agent.api.api:app --reload
```

API endpoint:

```
POST /ask
```

Example request:

```
{
  "query": "Research AI agent frameworks"
}
```

---

# 📚 Concepts Demonstrated

This project demonstrates core concepts of **Agentic AI**:

* Planner–Executor architecture
* ReAct reasoning
* Tool usage
* Tool registry pattern
* Memory system
* API-based agent service

---

# ⚠️ Current Limitations

This project is a **learning implementation**.

Future improvements:

* Vector memory (RAG)
* Multi-agent architecture
* Autonomous task loops
* Structured tool calling
* Long-term knowledge storage

---

# 🚀 Future Work

Planned upgrades:

* Vector database integration (FAISS / Chroma)
* Knowledge retrieval agents
* Multi-agent collaboration
* Autonomous research agents

---

# 📖 Learning Outcome

By building this project you learn:

* How modern AI agents are structured
* How LLMs perform reasoning and tool usage
* How to design modular agent architectures
* How production AI systems orchestrate agents
