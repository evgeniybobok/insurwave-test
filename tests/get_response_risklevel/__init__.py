import requests
import json

def get_response_risklevel(request_json):
    url = "http://127.0.0.1:8000/"
    response = requests.post(url=url, json=request_json)
    response_json = json.loads(response.text)
    return response_json['riskLevel']