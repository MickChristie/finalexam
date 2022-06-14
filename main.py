from fastapi import FastAPI

app1 = FastAPI()

listofbuyers=[]


@app1.get("/")
async def showMessage():
    return {"response": "this is the root. Nothing else."}
