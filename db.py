#from pyhdb import connect
from hdbcli import dbapi
import pandas as pd
from dotenv import load_dotenv
import os



def connect_to_database():
#carrega variáveis de ambiente do arquivo .env
    load_dotenv()

    connection = dbapi.connect(
        address = os.getenv('DB_HOST'),
        port = int(os.getenv('DB_PORT')),
        user = os.getenv('DB_USER'),
        password = os.getenv('DB_PASSWORD')

    )

    return connection

# cursor = connection.cursor()
# cursor.execute(
# """ 
# select 
# distinct stcd1 as cnpj_cpf
# from "NTR_S4_RT"."VT_SAPHANADB_KNA1"
# where land1 = 'BR'

# union 

# select 
# distinct stcd2 as cnpj_cpf
# from "NTR_S4_RT"."VT_SAPHANADB_KNA1"
# where land1 = 'BR'

# """

# )
# rows = cursor.fetchall()

# df = pd.DataFrame(rows, columns=[desc[0] for desc in cursor.description])

# print(df)

# # for row in rows:
# #     print(row)



# connection.close()
