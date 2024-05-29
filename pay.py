import requests

email = str(input())
sk = str(input())
amount = int(input())
url = ''
data = {
    'email': email,
    'amount': amount * 100
}

header = {
    'Authorization': 'Bearer'+ sk,
    'Content-Type': 'application/json'
}

response = requests.post(url, headers=header, data=data)