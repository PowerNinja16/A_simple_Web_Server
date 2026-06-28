import requests
response = requests.get('http://aosabook.org/en/500L/web-server/testpage.html')
print('status code:', response.status_code)
print('content length:', response.headers.get('content-length'))
print(response.text)