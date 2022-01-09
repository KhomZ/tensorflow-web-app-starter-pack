from fastapi import FastAPI
import uvicorn
# Uvicorn is a lightning-fast ASGI server implementation, using uvloop and httptools.

app = FastAPI()

@app.get('/index')
# get request api
# Similary, for post request we use app.post annotation
def hello_ikhomkodes(name: str):
    # return "Hello ikhomkodes!"
    return f"Hello {name}!"


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host='0.0.0.0')
