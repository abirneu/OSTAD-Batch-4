#Get request
"""
import requests

res = requests.get("https://jsonplaceholder.typicode.com/posts")

if res.status_code == 200:  # Checking for the correct status code
    print("Successful request:", res.json())  # Printing the JSON response
else:
    print("Failed to get data")

#post request
import requests

data = {
    "userId": 1,
    "title": "Test title",
    "body": "test body"
}

res = requests.post("https://jsonplaceholder.typicode.com/posts", json=data)  # Use `json` instead of `data`

if res.status_code == 201:  # 201 is correct for POST request
    print("Successful request:", res.json())  
else:
    print("Failed to send data")


#Patch request - small portion changes
import requests

data= {
    "title": "test"
}
res = requests.patch("https://jsonplaceholder.typicode.com/posts/1",data)  # Use `json` instead of `data`
if res.status_code == 200:  
    print("Successful")  
else:
    print("Failed to send data")


#Put request- changes all elements
import requests

data = {
    "userId": 1,
    "title": "Test title.......",
    "body": "test body........"
}

res = requests.put("https://jsonplaceholder.typicode.com/posts/1",data)  # Use `json` instead of `data`

if res.status_code == 200:  # 201 is correct for POST request
    print("Successful")  
else:
    print("Failed")

"""
import requests

data = {
    "userId": 1,
    "title": "Test title.......",
    "body": "test body........"
}

res = requests.delete("https://jsonplaceholder.typicode.com/posts/1")  # Use `json` instead of `data`

if res.status_code == 200:  # 201 is correct for POST request
    print("Successful")  
else:
    print("Failed")



