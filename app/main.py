
# import the fastAPI module first  
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from . routers import post, user, auth, vote


# models.Base.metadata.create_all(bind=engine)


#here we will create the app
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)



app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


'''
my_posts =[{"title": "title of post 1", "content":"content of post 1", "id": 1}, 
           {"title": "favorite foods", "content": "I like Pizza", "id": 2}] 


# here we will find the post id from the database
def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p
        

# Here we will find the index of the post from the database
def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p["id"] == id:
            return i

'''

# path operation
# request 'Get' method url: "/" 
@app.get("/")
def root():
    return {"message": "Hello World! Welcome to my API"}






