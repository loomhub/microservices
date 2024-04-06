from fastapi import FastAPI
import uvicorn
from mylib.logic import search_wiki
from mylib.logic import wiki as wikilogic
from mylib.logic import phrases

app = FastAPI()
@app.get("/")
async def root():
    return {"message":"Wikipedia API. Call /wiki or /search"}

@app.get("/search/{name}")
async def search(name:str):
    result = search_wiki(name)
    return {"result":result}

@app.get("/wiki/{name}")
async def wiki(name:str):
    result = wikilogic(name)
    return {"result":result}

@app.get("/phrase/{name}")
async def phrase(name:str):
    result = phrases(name)
    return {"result":result}

if __name__ == '__main__':
    uvicorn.run(app, port=8080,host='0.0.0.0')

#print(wiki())
