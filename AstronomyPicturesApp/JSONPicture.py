import json
import requests

API_KEY='8AqyU0ho2BcxC0pagCgHUtzgJ58dxn86Z9yRNk6A'
API_URL='https://api.nasa.gov/planetary/apod'

params={
    'api_key':API_KEY,
    'hd':'True',
    'count':100,
}

response=requests.get(API_URL,params=params)
json_data=json.loads(response.text)

print(json_data[0]['title'])
