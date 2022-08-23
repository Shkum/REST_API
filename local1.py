import requests

# res = requests.get()  # get data
# res = requests.post()  # send data
# res = requests.put()  # change data
# res = requests.delete()  # delete data


# res = requests.get('http://localhost:3000/api/courses')  #

res = requests.get('http://localhost:3000/api/courses/0')
print(res.json())

res = requests.get('http://localhost:3000/api/courses/1')
print(res.json())
print(res.json()['name'])

res = requests.delete('http://localhost:3000/api/courses/1')
print(res.json())

res = requests.delete('http://localhost:3000/api/courses/2')
print(res.json())

res = requests.post('http://localhost:3000/api/courses/3', {'name': "Golang", 'videos': 5})
res = requests.post('http://localhost:3000/api/courses/4', {'name': "PHP", 'videos': 20})
print(res.json())

res = requests.get('http://localhost:3000/api/courses/0')
print(res.json())
