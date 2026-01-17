import requests

API_KEY = "YOUR_API_KEY"
URL = "https://api.openai.com/v1/chat/completions"

def convert_code_online(code, task):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "gpt-4",
        "messages": [
            {"role": "user", "content": f"Convert this code from {task}:\n{code}"}
        ]
    }

    response = requests.post(URL, headers=headers, json=data)
    return response.json()["choices"][0]["message"]["content"]
