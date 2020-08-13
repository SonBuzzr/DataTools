import requests

payload = {'page': 2, 'count': 25}
login = {'username': 'admin', 'password':'password'}

get_request = requests.get('https://httpbin.org/get', params=payload)

post_request = requests.post('https://httpbin.org/post', data=login)

r_dict = post_request.json()
# print(post_request.json())
print(r_dict['form'])
