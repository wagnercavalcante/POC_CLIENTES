#from pyhdb import connect
from hdbcli import dbapi
import pandas as pd
from dotenv import load_dotenv
import os

from sqlalchemy import create_engine

#carrega variáveis de ambiente do arquivo .env
load_dotenv()

address = os.getenv('DB_HOST')
port = os.getenv('DB_PORT')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')

hana_url = f"hana://{user}:{password}@{address}:30415/?{db_name}"

engine = create_engine(hana_url)

with engine.connect() as connection:
    result = connection.execute('''select current.timestamp from dummy ''')
    for row in result:
        print(f"Conexão bem sucedida! Hora atual no SAP HANA: {row[0]}")