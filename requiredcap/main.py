from urllib import response
from fastapi import FastAPI
from pydantic import BaseModel
from factory import connector1
import uvicorn
import pandas as pd
import asyncio

api = FastAPI()
class Greendryfodder(BaseModel):
    Cattle_Weight:int
    Milking_ltrs:int
    

@api.get('/api/')
async def hello_home():
    return "Welcome to the feed API!"
    
@api.post('/api/GDC')
async def greendry(request: Greendryfodder):
    # print(request.dict())
    response_json = connector1.GDC(request.dict())
    # print(response_json)
    return response_json
    # return {}
if __name__ == '__main__':
    uvicorn.run(api,host='127.0.0.1',port=8080)


#server = uvicorn.run(api)
