from pyhdb import connect

connection = connect(
    host="unify.nutrien.com",
    port=30415,
    user="SVC_PBI_BR_DEVELOPER",
    password="Nutr13n@PBI.BR.D3v3l0pPRD"
)

cursor = connection.cursor()
cursor.execute("""select 
distinct stcd1 as cnpj_cpf
from "NTR_S4_RT"."VT_SAPHANADB_KNA1"
where land1 = 'BR'

union 

select 
distinct stcd2 as cnpj_cpf
from "NTR_S4_RT"."VT_SAPHANADB_KNA1"
where land1 = 'BR'""")
rows = cursor.fetchall()
for row in rows:
    print(row)
connection.close()
