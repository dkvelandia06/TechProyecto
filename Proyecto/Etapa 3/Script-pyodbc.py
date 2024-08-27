import pyodbc
import pandas as pd
from sqlalchemy import create_engine

# Configuración de la conexión
server = r'Nombre_servidor'
database = 'Nombre_BD'
username = 'usuarioBD'
password = 'contrasenaBD'
driver='ODBC Driver 17 for SQL Server'
connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

# Conexión a la base de datos
conn = pyodbc.connect(connection_string)
cursor = conn.cursor()

engine = create_engine(f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver={driver}')

df=pd.read_csv(r'D:\Curso MINTIC Analisis datos\Analisis datos\Proyecto 3\data\data_combinada.csv')
df.columns = ['Date', 'Symbol', 'PriceClose']
def load_data_to_sql(engine, df, table_name):
    """Cargar los datos de un DataFrame a una tabla d SQL SERVER"""
    try:
        df.to_sql(table_name, con=engine, if_exists='replace', index=False)
        print(f"Datos cargados correctamente en la tabla {table_name}")
    except Exception as e:
        print(f"Error al cargar los datos: {e}")
df.to_sql('Companies', con=engine, if_exists='replace', index=False)
load_data_to_sql(engine, df, 'Companies')


df=pd.read_csv(r'D:\Curso MINTIC Analisis datos\Analisis datos\Proyecto 3\empresasSp500.csv')
df=df.drop(columns=['Presentación ante la SEC','Sub-industria GICS','Fecha de incorporación','Clave de índice central'])

df.columns=['Symbol', 'Company','Sector','Headquarters','Fechafudada']
def load_data_to_sql(engine, df, table_name):
    """Cargar los datos de un DataFrame a una tabla d SQL SERVER"""
    try:
        df.to_sql(table_name, con=engine, if_exists='replace', index=False)
        print(f"Datos cargados correctamente en la tabla {table_name}")
    except Exception as e:
        print(f"Error al cargar los datos: {e}")
df.to_sql('CompanyProfiles', con=engine, if_exists='replace', index=False)
load_data_to_sql(engine, df, 'CompanyProfiles')

# Cerrar la conexión
cursor.close()
conn.close()
