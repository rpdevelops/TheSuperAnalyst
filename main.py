from vanna.remote import VannaDefault
from vanna.flask import VannaFlaskApp
from config.database_config import DatabaseConfig
from config.api_config import ApiConfig
from config.my_vanna import MyVanna
from config.auth import SimplePassword
from config.users import Users

## Criação dos Objetos de Configuração
dbConfig = DatabaseConfig()
apiConfig = ApiConfig()
user_teste = Users()
moddel_name = "gpt-4o"
vn = MyVanna(config={'api_key':apiConfig.api_key,'model': moddel_name})

## Conexão com o Banco de Dados MySQL de Destino
vn.connect_to_mysql(host=dbConfig.host,dbname=dbConfig.dbname,user=dbConfig.user,password=dbConfig.password,port=dbConfig.port)

## Configuração e Inicialização da Aplicação
app = VannaFlaskApp( vn=vn,
    auth=SimplePassword(users=[{"email": user_teste.email, "password": user_teste.password}]),
    allow_llm_to_see_data=True,
    logo='https://iili.io/d7388x9.jpg',
    title="FintechX Super Analyst",
    subtitle='A IA com tecnologia Text2SQL ideal para sua tomada de Decisões! Comece fazendo uma pergunta sobre sua base de dados:',
    show_training_data=True,
    sql=True,
    table=True,
    chart=True,
    summarization=False,
    ask_results_correct=True,
).run()