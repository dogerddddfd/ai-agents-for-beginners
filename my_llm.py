import requests
import json
import dotenv
import os
dotenv.load_dotenv()

url = "" + os.getenv("API_URL") + "/chat/completions"
model = os.getenv("MODEL_FREE_8B")
api_key = os.getenv('API_KEY')

payload = {
    "model": model,
    "messages": [
        {
            "role": "user",
            "content": "test"
        }
    ],
    "stop": []
}
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

def llm(messages):
  payload["messages"] = messages
  response = requests.request("POST", url, json=payload, headers=headers)
  if response.status_code != 200:
    raise Exception(response.text)
  return response

def get_reasoning_content(response):
  json_data = json.loads(response.text)
  if json_data["choices"][0]["message"]["reasoning_content"] :
    return json_data["choices"][0]["message"]["reasoning_content"]
  else:
    return ""

def get_content(response):
  json_data = json.loads(response.text)
  if json_data["choices"][0]["message"]["content"] :
    return json_data["choices"][0]["message"]["content"]
  else:
    return ""


if __name__ == "__main__":
    # 简单的连接测试：发送一条消息并打印响应内容
    try:
        resp = llm([{"role": "user", "content": "ping"}])
        print("连接成功，响应内容：", get_content(resp))
    except Exception as e:
        print("连接失败：", e)
