import requests
import json


def test_send_comment():
    response = requests.get("https://preprod-api.metamorph.caifudamofang.com/api/v1/media/public/videos")
    json_data = response.json('')
    print(json.dumps(json_data, indent = 4, sort_keys=True))