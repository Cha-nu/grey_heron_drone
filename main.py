import uvicorn
from fastapi import FastAPI
import droneServer

app = FastAPI()
app.include_router(droneServer.router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
    print("protocol online")