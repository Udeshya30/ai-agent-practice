from fastapi import FastAPI
from pydantic import BaseModel

from ai_agent_01.agent import run_agent

app = FastAPI()


class QueryRequest(BaseModel):
    query: str


@app.get("/")
def home():
    return {"message": "AI Research Agent API running"}


@app.post("/ask")
def ask_agent(request: QueryRequest):

    result = run_agent(request.query)

    return {
        "query": request.query,
        "answer": result
    }