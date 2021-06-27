from fastapi import FastAPI,Body,status
from .models import PostSchema,UserLoginSchema,UserSchema
from .auth.auth_handler import signJWT
from typing import List


app=FastAPI()


posts=[
    {
        "id":1,
        "title":"JWT Authentication with FastAPI",
        "content":"Lorem Ipsum whatever"
    }
]


users=[]

def checkUser(data:UserSchema)->bool:
    for user in users:
        if (user.email == data.email) and (user.password == data.password):
            return True

        else:
            return False


@app.get('/',tags=["root"])
def hello()->dict():
    return {"message": "Hello World"}


@app.get('/posts',response_model=List[PostSchema])
def getAllPosts()->dict:
    return posts


@app.get('/post/{post_id}')
def getPost(post_id:int)->dict:
    if post_id > len(posts):
        return {"message": "Post not found"}
    
    for post in posts:
        if post["id"] == post_id:
            return {"post":post}


@app.post('/posts')
def createPost(post:PostSchema)->dict:

    
    new_post={
        "id":len(posts)+1,
         "title":post.title,
         "content":post.content
        }

    posts.append(new_post)

    return {"message": "Post created"}


@app.post('/signup',status_code=201)
def create_user(user:UserSchema):
    users.append(user)
    return signJWT(user.id)


@app.post('/login')
def user_login(user:UserLoginSchema):
    if checkUser(user):
        return signJWT(user.email)

    return {"error":"Invalid Credentials"}




