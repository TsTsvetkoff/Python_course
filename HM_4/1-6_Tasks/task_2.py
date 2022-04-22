"""
2. Play with the requests library. Learn using API’s: e.g. https://swapi.co/
"""

import requests
import json

# 1. Get Requests
get_details = requests.get("https://reqres.in/")
#print(get_details.content)



# 2. POST Requests

data = {
    "name": "Peshkata",
    "job": "Shefche"
}
my_post = requests.post("https://reqres.in/api/users", data)
json_data = json.loads(my_post.text)    # Here we convert the response to dict
print(json_data)

#Now we want to get the dinamic id
dynamic_id = json_data.get('id')
print(dynamic_id)



#check if created
is_created = requests.get(f"https://reqres.in/api/users/{dynamic_id}")
print(is_created)

# This site https://reqres.in/ hos bad api mocking



