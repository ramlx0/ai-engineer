import requests

def fetch_todo(todo_id: int) -> dict:
    url = f'https://jsonplaceholder.typicode.com/todos/{todo_id}'

    #git request code 
    response = requests.get(url)

    response.raise_for_status()
    return response.json()