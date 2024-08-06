from dotenv import load_dotenv
import os
load_dotenv('enviroments/user-config.env')
class Users:
    def __init__(self):
        self.email = os.getenv('EMAIL')
        self.password=os.getenv('PASSWORD')