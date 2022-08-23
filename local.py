import requests

# res = requests.get()  # get data
# res = requests.post()  # send data
# res = requests.put()  # change data
# res = requests.delete()  # delete data


res = requests.get('http://localhost:3000/api/main')  #

print(res.json())
