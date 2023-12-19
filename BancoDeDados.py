import os
import pandas as pd
from sqlalchemy import create_engine

import mysql.connector

# Caminho para a pasta com os arquivos .xlsx
pasta_arquivos = r'C:\Users\alan.mendes\OneDrive - Sicoob\Área de Trabalho\Bases Banco'

# Obter lista de arquivos .xlsx na pasta
arquivos_xlsx = [arquivo for arquivo in os.listdir(pasta_arquivos) if arquivo.endswith('.xlsx')]

print(arquivos_xlsx)

# In[34]:

# Conexão com o banco de dados
#engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')
#engine = create_engine("mysql+pymysql://desenvolvimento_db:D3WLLGtyvwHkRja@desenvolvimento.unicb.coop.br:3306/desenvolvimento_db")
engine = create_engine("mysql+pymysql://sql_devnegocios:MPhxbaNaM82BaJDPA@db-transformacao-digital.cluster-cfddezkzzs9e.sa-east-1.rds.amazonaws.com:3306/sql_devnegocios")
#engine = create_engine("mysql+pymysql://sql_devnegocios:MPhxbaNaM82BaJDPA@db-transformacao-digital.cluster-cfddezkzzs9e.sa-east-1.rds.amazonaws.com:3306/ic_ferramentas")
# In[39]:

# Iterar sobre os arquivos .xlsx e carregar para o banco de dados
for arquivo in arquivos_xlsx:
    caminho_arquivo = os.path.join(pasta_arquivos, arquivo)
    df = pd.read_excel(caminho_arquivo)
    #df = df.replace({',': '.'}, regex=True)
    #df['Valor_Transacao'] = df['Valor_Transacao'].astype(float)
    df.to_sql('MensalFechamentodeCredito', engine, if_exists='append', index=False)

# Fechamento da conexão com o banco de dados
engine.dispose()

print('Dados carregados com sucesso para o banco de dados!')

# In[ ]:
 