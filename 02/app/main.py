from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/api")
async def root():
    return {"message": "You are doing great with FastAPI!"}

@app.get("/api/{name}")
async def return_name(name: str):
    return {
        "name": name,
        "message": f"Hello, {name}!"
    }

@app.get("/joke")
async def return_joke():
    jokes = [
        "Why do we tell actors to 'break a leg?' Because every play has a cast.",
        "Why don't scientists trust atoms? Because they make up everything!",
        "How do you organize a space party? You planet!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "What do you call a fish wearing a crown? A kingfish!",
        "What did the ocean say to the beach? Nothing, it just waved!",
    ]
    return {
        "joke": random.choice(jokes)
    }
    
    """
    Comandos importantes:
        iniciar o serviço com servidor local: uvicorn app.main:app --host 0.0.0.0 --port 8087
    """