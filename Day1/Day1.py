from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def show():
    return {
        "message":"This is my first fastapi "
    }
