import json
import requests

def get_access_token(URL, headers, body):
    ''' 토큰 발급 '''
    URI = f"{URL}/oauth2/tokenP"
    
    response = requests.post(URI, headers=headers, data=json.dumps(body)).json()
    
    return response['access_token']

def hashkey():
    pass