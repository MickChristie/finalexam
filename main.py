from fastapi import FastAPI

app1 = FastAPI()

listofbuyers=[]


@app1.get("/")
async def showMessage():
    return {"response": "this is the root. Nothing else."}

@app1.get("/buyers")
async def getBuyers1():
    return getBuyers()

@app1.post("/buyers")
async def addBuyer(anewbuyer: str, count: int = 1):
    result = False
    message = "Not specified"
    if anewbuyer in listofbuyers:
        listofbuyers[anewbuyer] = listofbuyers[anewbuyer] + count
        result = True
        message = f"Existing and added item(s): {anewbuyer}."
    else:
        result = True
        message = f"Successfully added: {anewbuyer}."
        listofbuyers[anewbuyer] = count

    return {"result": result, "message": message, "current buyers": listofbuyers}

def getBuyers():
    return (listofbuyers)

