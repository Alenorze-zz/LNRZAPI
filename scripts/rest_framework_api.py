import json
import requests
import os


AUTH_ENDPOINT = "http://127.0.0.1:8000/api/auth/jwt/"
REFRESH_ENDPOINT = AUTH_ENDPOINT + "refresh/"
ENDPOINT = "http://127.0.0.1:8000/api/status/"

image_path = os.path.join(os.getcwd(), "logo.jpg")

headers = {
    "Content-Type": "application/json"
}

data = {
    'username': 'cfe',
    'password': 'learncode'
}

r = requests.post(AUTH_ENDPOINT, data=json.dumps(data), headers=headers)
token = r.json()['token']


# refresh_data = {
#     'token': token
# }

# new_response = requests.post(REFRESH_ENDPOINT, data=json.dumps(refresh_data), headers=headers)
# new_token = new_response.json()#['token']

# print(new_token)




headers = {
    #"Content-Type": "application/json",
    "Authorization": "JWT " + token,
}

with open(image_path, 'rb') as image:
    file_data = {
        'image': image
    }
    data = {
        "content": "Updated description"
    }
    json_data = json.dumps(data)
    posted_response = requests.put(ENDPOINT + str(37) + "/", data=data, headers=headers, files=file_data)
    print(posted_response.text)


headers = {
    #"Content-Type": "application/json",
    "Authorization": "JWT " + token,
}

data = {
    "content": "Updated description"
}
json_data = json.dumps(data)
posted_response = requests.put(ENDPOINT + str(37) + "/", data=data, headers=headers)
print(posted_response.text)
