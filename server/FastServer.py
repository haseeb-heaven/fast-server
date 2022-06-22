"""
Info: Simple API based server in Python 3 using `FastAPI v0.78.0` framework.
Author: Haseeb Mir (haseebmir.hm@gmail.com)
"""

from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from email.utils import parseaddr #Email Validator.
import json #For Json Parsing.
from json import JSONEncoder
import os
import uvicorn

#Main app of FastApi-Server.
app = FastAPI()
server_file = os.path.splitext(os.path.basename(__file__))[0] #Filename without extension.
    
#User class.
class User(BaseModel):
    name: str
    age: int
    gender: str
    email:str
    phone:str
    address: str

# subclass UserEncoder
class UserEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__

#Users data storage.
users = []
json_dir = "fast-data"
json_path = json_dir + "/users.json"

#Methods and Class for saving and loading persistent data of server.
def save_users(json_path:str,data,append:bool=False):
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4,cls=UserEncoder)

def load_users(json_path:str):
    if not os.path.exists(json_path):
        return []
    with open(json_path,'r', encoding='utf-8') as fp:
        data = json.loads(fp.read())
        return data

#Dict convert to class object (User).
class DictConv(object):
      
    def __init__(self,data):
          
        for key in data:
            setattr(self, key,data[key])

#Root of Server.
@app.get("/")
async def root():
    try:
        global users
        
        #Create Json directory.
        if not os.path.exists(json_dir):
            os.mkdir(json_dir)
        
        if len(users) > 0:
            save_users(json_path,users,True)
            return users
        else:
            data_list = load_users(json_path)
            for data in data_list:
                user = DictConv(data)
                users.append(user)
                
            return {"data": "No users data found - Server Maintenance."}
    except Exception as ex:
        print("Exception in server: " + str(ex))

#Retrieve user from Id/username.
@app.get("/user/")
async def get_user(id: Optional[int] = -1, name: Optional[str] = None):
    global users
    
    if id != -1:
        if id > len(users):
            return {"data":  "Error user id is invalid"}
        else:
            return users[id]
    elif name is not None:
        for user in users:
            if user['name'].casefold() == name.casefold():
                return user
        return {"data":  "Error username is invalid"}
    else:
        return {"data": "Error no parameters were passed"}

#Adding new user.
@app.post("/add-user/")
async def add_user(user: User):
    global users
    
    if user in users:
        return {"data": "Error user already exist"}
    else:
        if len(user.name) > 0 and '@' in parseaddr(user.email)[1] and '+' in parseaddr(user.phone)[1] and user.age > 0:
            users.append(user)
            return {"data": "User '" + user.name + "' added success"}
        else:
            return {"data": "Error: User '" + user.name + "' cannot be added"}

#Update user.
@app.patch("/update-user/")
async def update_user(id:int,name:str,age: Optional[int] = None):
    global users
    if id > len(users):
        return {"data":  "Error user id is invalid"}
    else:
        users[id].name = name
        users[id].age = age
        return {"data": "User '" + users[id].name + "' updated success"}

#Remove user.
@app.delete("/remove-user/")
async def remove_user(id:int):
    global users
    if id > len(users):
        return {"data": "Error user id is invalid"}
    else:
        user = users[id].name
        del users[id]
        return {"data": "User '" + user + "' removed success"}

#Show Server info.
@app.get("/server-info/")
async def get_server_info():
    global users
    return {
            "server": "Python 3 using `FastAPI v0.78.0` framework",
            "database": "Server Database file '"  + json_path + "'",
            "source": "Server file '"  + server_file + ".py'",
            "users": "Total " + str(users.__len__()) + " Users in Server Database",
            }

#Null the DB of server.
@app.get("/null/")
async def null():
    global users
    users.clear()
    save_users(json_path,users)
    return {"data": "Server Database cleared success"}

#Main server app.
if __name__ == "__main__":
    uvicorn.run(server_file + ":app", debug=True, reload=True) #Start the server with Debug and Reload flags.