import requests
import json

API_ENDPOINT = ""

def get_token(user,request):
    uri= 'http://' + request.get_host() + "/user/gettoken/"
    data ={'username':user['username'],'password':user['password']}
    response = requests.post(url=uri,data=data)
    result = json.loads((response.content).decode("utf-8"))
    return result['access']

