import requests
r = requests.post('http://localhost:8080/testRedis/getRedisByKey?key=ccc')
print(r.json())