import requests
import random
import string
import json

# Base URL
url = 'https://fast-server.vercel.app'


# Function to generate random data
def generate_random_data():
    name = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=5))
    age = random.randint(20, 50)
    gender = random.choice(['male', 'female'])
    email = name + '@gmail.com'
    phone = '+91' + ''.join(random.choices(string.digits, k=10))
    address = 'home ' + str(random.randint(1, 100))
    return {
        'name': name,
        'age': age,
        'gender': gender,
        'email': email,
        'phone': phone,
        'address': address
    }

  
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

  
def show_users(id, indent:int=4):
    user_url = url + f"/user/?id={id}"
    req = requests.get(user_url)
    print(f"Showing users with url: {user_url}")
    if req:
        req_json = req.json()
        print(json.dumps(req_json,indent=indent,sort_keys=True))

def print_response(data:json):
    print(data)

# Main app.
if __name__ == "__main__":
    try:
        #Add 5 users.
        for i in range(5):
            user = generate_random_data()
            data = add_user(user)
            print_response(data)

        # Show users.
        for i in range(5):
            show_users(i)
    
    except Exception as ex:
        print("Exception occurred: " + str(ex))
