import requests
import json

url = "http://192.168.43.44:7860/sdapi/v1/txt2img"

payload = json.dumps({
  "prompt": "ultra realistic close up portrait ((beautiful pale cyberpunk female with heavy black eyeliner))",
})

headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response)