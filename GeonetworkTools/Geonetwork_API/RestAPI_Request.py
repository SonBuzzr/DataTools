import requests

payload = {'page': 2, 'count': 25}
login = {'username': 'admin', 'password':'password'}

get_request = requests.get('https://httpbin.org/get', params=payload)
print(get_request.url)

post_request = requests.post('https://httpbin.org/post', data=login)
print(post_request.url)
