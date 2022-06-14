from fastapi import FastAPI

app1 = FastAPI()

listofbuyers=[]
listofproducts=[]
boughtproduct = {}

@app1.get("/")
async def showMessage():
    return {"response": "this is the root. Nothing else."}

@app1.get("/buyers")
async def getBuyers1():
    return getBuyers()


@app1.get("/products")
async def getProducts1():
    return getProducts()

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

@app1.post("/products")
async def addProduct(anewproduct: str, count: int = 1):
    result = False
    message = "Not specified"
    if anewprodyct in listofproducts:
        listofproducts[anewproduct] = listofproducts[anewproduct] + count
        result = True
        message = f"Existing and added item(s): {anewproduct}."
    else:
        result = True
        message = f"Successfully added: {anewproduct}."
        listofproducts[anewproduct] = count

    return {"result": result, "message": message, "current products": listofproducts}



def getBuyers():
    return (listofbuyers)

def getProducts():
    return (listofproducts)

