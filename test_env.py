import os 
from dotenv import load_dotenv

load_dotenv()

testkey = os.getenv('TEST_KEY')
print(testkey)