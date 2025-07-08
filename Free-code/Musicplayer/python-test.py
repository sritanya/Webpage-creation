import requests

url = "https://workwithus.lucioai.com/get-started"
payload = {
    "name": "Pattanam Chaitanya Sri",
    "email": "pattanamchaitanyasri25@gmail.com"
}

response = requests.post(url, json=payload)
print("Status Code:", response.status_code)
print("Response:", response.text)


https://workwithus.lucioai.com/get-started/{"name": "Pattanam Chaitanya Sri", "email": "pattanamchaitanyasri25@gmail.com"}