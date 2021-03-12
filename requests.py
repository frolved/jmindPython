import requests
import json

def test_first():
    r = json.loads(requests.get("https://qa-api.metamorph.caifudamofang.com/api/v1/media/public/version"))
    print(r)