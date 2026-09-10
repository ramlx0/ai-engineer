from dataclasses import dataclass

@dataclass
class ChatMessage:
    role : str
    content : str 

class ConversationManager:
    def __init__(self , model_name : str):
        self.model_name = model_name
        self.messages : list[ChatMessage] = []

    def add_message(self, role:str , content:str ):
        new_message = ChatMessage(role = role , content= content)
        self.messages.append(new_message)

    def get_meesage_count(self) -> int:
        return len(self.messages)

    def to_dict_list(self) -> list[dict]:
        formatted = []
        for msg in self.messages:
            formatted.append({
                'role': msg.role,
                'content' : msg.content
            })
        return formatted

# execution & testing

if __name__ == '__main__':
    manager = ConversationManager(model_name='gpt-4o')
    manager.add_message('system','You are a helpful AI assistant.')
    manager.add_message('user','explain oop in python')

    print(f'model: {manager.model_name}')
    print(f'total message : {manager.get_meesage_count()}')
    print('api payload:', manager.to_dict_list())