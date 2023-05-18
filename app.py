from fastapi import FastAPI
import uvicorn


app = FastAPI()


@app.get("/")
def read_main():
    return {"message": "This is your main app"}
