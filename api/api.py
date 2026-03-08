from fastapi import FastAPI
from pydantic import BaseModel

from agent.controller import run_agent
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    query: str


@app.post("/ask")
def ask_agent(request: QueryRequest):

    answer = run_agent(request.query)

    return {
        "query": request.query,
        "answer": answer
    }