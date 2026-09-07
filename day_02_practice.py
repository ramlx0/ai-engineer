import json 
import requests 

raw_llm_response = '{"model": "gpt-4o", "content": "hello i am ready", "token": 25}'

parsed_respose = json.loads(raw_llm_response)

class LLMRespose:
    def __init__(self, model: str , content : str ,token : int ) -> None:
        self.model = model 
        self.content = content
        self.token = token

response_obj = LLMRespose(
    model=parsed_respose['model'],
    content=parsed_respose['content'],
    token=parsed_respose['token']
)

print(response_obj.content)

url = "https://jsonplaceholder.typicode.com/todos/1"
api_response = requests.get(url)
api_response.raise_for_status()

todo_data = api_response.json()
print("Fetched Title:", todo_data["title"])