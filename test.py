import requests

BASE = 'http://127.0.0.1:5000/'

data = [
    {'likes': 10, 'name': 'math', 'views': 100},
    {'likes': 20, 'name': 'pi', 'views': 200},
    {'likes': 30, 'name': 'std', 'views': 300}
]

for i in range(len(data)):
    response = requests.put(BASE + 'video/' + str(i), data[i])
    print(response.json())

input()
response = requests.get(BASE + 'video/2')
print(response.json())
input()
response = requests.patch(BASE + 'video/2', data[0])
print(response.json())
input()
response = requests.get(BASE + 'video/2')
print(response.json())