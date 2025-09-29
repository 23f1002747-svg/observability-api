from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Deployment-ready observability API running"}
