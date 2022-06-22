"""
Info : FastClient in Python for FastApi connection.
Author: Haseeb Mir.
"""
import json
import requests
url = "http://localhost:8000"

def add_user(user: dict):
    user_url = url + "/add-user/"
    req = requests.post(url=user_url, json=user)
    return req.json()

def update_user(id:int=0,name:str="",age:int=0):
    user_url = url + "/update-user/?id=" + str(id) + "&name=" + name + "&age=" + str(age)
    req = requests.patch(url=user_url)
    return req.json()

def remove_user(id:int=0):
    user_url = url + "/remove-user/?id=" + str(id)
    req = requests.delete(url=user_url)
    return req.json()

def show_users(indent:int=4):
    req = requests.get(url)
    
    if req:
        req_json = req.json()
        print(json.dumps(req_json,indent=indent,sort_keys=True))

def print_response(data:json):
    print(data["data"])


# Main app.
if __name__ == "__main__":
    try:
        #Add user.
        user = {'name': "Haseeb", 'age': 25, 'gender': 'M','email': "hm@gmail.com", 'phone': "+971-54545454", 'address': "DXB"}
        data = add_user(user)
        print_response(data)

        #Update user.
        #data = update_user(0,'Akil',25)
        #print_response(data)
         
        #Remove user.
        #data = remove_user(0)
        #print_response(data)
         
        # Show users.
        req = show_users()
        
    except Exception as ex:
        print("Exception occurred: " + str(ex))
