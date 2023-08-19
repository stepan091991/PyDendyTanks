import requests
print(requests.post("http://127.0.0.1:5000/api/upload_data/",{"name":"test"}).content)