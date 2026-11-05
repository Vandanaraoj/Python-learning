import requests
url="https://jsonplaceholder.typicode.com/posts"
payload={"title":"python course","body":"Rahul is learning python","userId":1}
response=requests.post(url,json=payload)
print(response.status_code)
print(response.json())