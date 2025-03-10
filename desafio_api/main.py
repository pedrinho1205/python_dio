from fastapi import FastAPI

app = FastAPI(title="WorkoutApi")


@app.get("/")
def home():
    return {"message": "API funcionando!"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000,
                log_level="info", reload=True)
