from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return { "msg": "hej  local docker" }


@app.get("/api/ip")
def ip():
    return { "ip": "hello ip" }


@app.get("/hello")
def hello():
    return { "msg": "helllllo" }