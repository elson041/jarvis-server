from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Jarvis server is running 🚀"}

@app.post("/command")
def process_command(command: str):
    # Yaha baad me AI logic add karenge
    return {"response": f"Jarvis ne suna: {command}"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
