from dotenv import load_dotenv
import os
load_dotenv('enviroments/db-config.env')
class DatabaseConfig:
    def __init__(self):
        self.host = os.getenv('DB_HOST')
        self.dbname=os.getenv('DB_NAME')
        self.user=os.getenv('DB_USER')
        self.password=os.getenv('DB_PASS')
        self.port=int(os.getenv('DB_PORT'))