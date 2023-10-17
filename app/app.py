from fastapi import FastAPI
from handler import app as handler_app

app = FastAPI()

app.mount("/admin", handler_app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
