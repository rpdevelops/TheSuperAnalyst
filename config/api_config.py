from dotenv import load_dotenv
import os
load_dotenv('enviroments/api-config.env')
class ApiConfig:
    def __init__(self):
        self.api_key = os.getenv('API_KEY')