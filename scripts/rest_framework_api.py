import json
import requests
import os


ENDPOINT = "http://127.0.0.1:8000/api/status/"

image_path = os.path.join(os.getcwd(), "logo.jpg")



get_endpoint =  ENDPOINT + str(12)
post_data = json.dumps({"content": "Some random content"})


r = requests.get(get_endpoint)
print(r.text)



r2 = requests.get(ENDPOINT)
print(r2.status_code)



post_headers = {
    'content-type': 'application/json'
}

post_response = requests.post(ENDPOINT, data=post_data, headers=post_headers)
print(post_response.text)
