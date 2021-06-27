from pydantic import BaseModel ,Field,EmailStr

class PostSchema(BaseModel):
    id:int=Field()
    title:str=Field(max_length=100)
    content:str=Field(max_length=10000)


    class Config:
        schema_extra={
            "example":{
                "title":" a title",
                "content":"..."
            }
        }


class UserSchema(BaseModel):
    id:int
    username:str=Field(max_length=10)
    email:str=Field(max_length=80)
    password:str=Field(max_length=10000)


    class Config:
        schema_extra={
            "example":{
                "id":1,
                "username":"user",
                "email":"user@example.com",
                "password":"wateva password"
            }
        }



class UserLoginSchema(BaseModel):
    email:str=Field(max_length=80)
    password:str=Field(max_length=10000)


    class Config:
        schema_extra={
            "example":{
                "email":"user@example.com",
                "username":"user",
            }
        }