from fastapi import FastAPI
app = FastAPI()

#First code for API
@app.get("/hello-world")
def hello_world():
    return {"message" : "Hello World"}