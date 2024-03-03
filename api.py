import requests
API_TOKEN = "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"
headers = {"Authorization": f"Bearer {API_TOKEN}"}
API_URL = "https://api-inference.huggingface.co/models/brianc07/easypass4"
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()
data = query({"inputs": "Generate a mechanics problem that involves angular momentum and moment of inertia, only output the problem and nothing else."})
print(data)
