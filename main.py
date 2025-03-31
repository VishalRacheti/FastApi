from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI() # Create the instance of FASt API

## The app instance is the main component of FastApi application .It is used to configure the application 
class Custom(BaseModel):
    name: str
    age: int


#/ ping is the path of the end point

# @app.get() is the decorator is used to define an endpoint 
@app.get('/ping')
async def root ():
    return {"message": "Hello World  !!!"}

@app.get('/')
async def pong() :
    return {"message": "pong"} 

@app.get("/blog/comments")
async def read_comments ():
    return {"message" : "This is the comments section"}

@app.get('/blog/{blog_id}')
async def read_blog (blog_id : int):
    return {'blog_id': blog_id}


#Qurey Params

@app.post('/blogs/{blog_ids}')
async def read_qurey (blog_ids : int , request_body: Custom , q : str = None , name: str = " "):
    print(request_body.age)
    print (q, name)
    return {"blog_ids" : blog_ids, "q" : q , "Name" : name}

