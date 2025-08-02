import requests

url = "http://www.w3schools.com/python/python_inheritance.asp"
res = requests.get(url)
print(res.status_code)
print(res.text)