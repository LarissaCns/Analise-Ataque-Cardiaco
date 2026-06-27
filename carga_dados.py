import os
import pandas as pd
from sqlalchemy import create_engine

NOME_FICHEIRO = 'heart_limpo.csv'

if not os.path.isfile(NOME_FICHEIRO):
    print(f"Erro: O ficheiro '{NOME_FICHEIRO}' não foi encontrado.")
else:
    print(f" ler o ficheiro {NOME_FICHEIRO}...")
    df = pd.read_csv(NOME_FICHEIRO)


    engine = create_engine('postgresql://admin:admin@localhost:5432/projetos')

    NOME_TABELA = 'heart_attack_data'
    print(f"A carregar os dados na tabela '{NOME_TABELA}'...")
    df.to_sql(NOME_TABELA, engine, if_exists='replace', index=False)

    print("Sucesso: Os dados foram carregados na base de dados PostgreSQL.")
