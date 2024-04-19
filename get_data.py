from db import connect_to_database
import pandas as pd

def execute_queries(queries):
    # Conecta ao banco de dados
    connection = connect_to_database()

    try:
        # Cria um cursor para executar as consultas
        cursor = connection.cursor()

        # Lista para armazenar os DataFrames resultantes de cada consulta
        result_dfs = []

        # Itera sobre as consultas fornecidas
        for query in queries:
            # Executa a consulta
            cursor.execute(query)

            # Obtém os resultados, se houver
            results = cursor.fetchall()

            # Converte os resultados para um DataFrame do Pandas
            df = pd.DataFrame(results)

            # Adiciona o DataFrame resultante à lista de resultados
            result_dfs.append(df)

        return result_dfs

    finally:
        # Fecha a conexão com o banco de dados, independentemente de ocorrerem erros
        connection.close()


# Exemplo de uso da função execute_query
queries = [""" 
            select 
            distinct stcd1 as cnpj_cpf
            from "NTR_S4_RT"."VT_SAPHANADB_KNA1"
            where land1 = 'BR'

            union 

            select 
            distinct stcd2 as cnpj_cpf
            from "NTR_S4_RT"."VT_SAPHANADB_KNA1"
            where land1 = 'BR'

"""
,
"""
select distinct source, max(last_etl_date), max(dt_faturamento) from "N07_OTHER_STG"."LATAM.BR.SALES.MODEL::TABLES_ODS.FATURAMENTO_EVT"
where to_dats(last_etl_date) = current_date
group by source
order by source asc
"""


]
result_df = execute_queries(queries)
print(result_df)