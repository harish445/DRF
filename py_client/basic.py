import requests

endpoint = 'https://httpbin.org/'

get_response = requests.get(endpoint)  # HTTP request
print(get_response.text)    # print raw text response