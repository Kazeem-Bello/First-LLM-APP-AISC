from fastapi import FastAPI, Request
import uvicorn
from simple import *

app = FastAPI()

@app.get("/healthz")
async def health():
    return{
        "application": "Simple LLM API",
        "message": "running succesfully"
    }

@app.post("/chat")
async def generate_chat(request: Request):
    query = await request.json()
    model = query["model"]

    try:
        temperature = float(query["temperature"])
    except:
        return {
            "error": "Invalid input, pass a number between 0 and 1"
        }
    
    if model not in models:
        return {
            "error": "You did not pass a correct model code!"
        }
    
    response = generate(query["question"], model, temperature = temperature)

    return {
        "status": "success",
        "response": response
    }

if __name__ == "__main__":
    import uvicorn
    print("Starting LLM API")
    uvicorn.run(app, host="0.0.0.0", reload=True)