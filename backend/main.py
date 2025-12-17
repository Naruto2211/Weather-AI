from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agent import get_agent_executor
import os
from dotenv import load_dotenv

load_dotenv()

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

class QueryResponse(BaseModel):
    response: str

@app.post("/chat", response_model=QueryResponse)
async def chat(request: QueryRequest):
    if not os.environ.get("OPENROUTER_API_KEY"):
         raise HTTPException(status_code=500, detail="OPENROUTER_API_KEY not set")
    
    try:
        agent = get_agent_executor()
        # LangGraph invoke returns a dictionary with 'messages'
        # simpler input format: {"messages": [("user", request.query)]}
        result = agent.invoke({"messages": [("user", request.query)]})
        
        # The last message should be the AI response
        last_message = result["messages"][-1]
        return QueryResponse(response=last_message.content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
