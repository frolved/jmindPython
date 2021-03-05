import json
from random import randrange
import requests

def test_send_comment():
    response = requests.get("https://preprod-api.metamorph.caifudamofang.com/api/v1/media/public/videos")
    json_data = response.json()
    ids = len(json_data["data"])
    random_id = randrange(ids)
    print(random_id)
    print(ids)
    print(json.dumps(json_data, indent = 4, sort_keys=True))
    comment = requests.post("https://preprod-api.metamorph.caifudamofang.com/api/v1/chat/private/message",)
    juul.make_post