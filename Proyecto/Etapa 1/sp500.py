# -*- coding: utf-8 -*-
"""
Diana Karina Velandia
Juan David Zamudio 
Nicolas Leguizamon
"""
import yfinance as yf 
import pandas as pd
import os
import logging



log_dir = './logs'
data_dir = './data'

if not os.path.exists(log_dir):
    os.makedirs(log_dir)
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

log_filename = os.path.join(log_dir, 'etl_process.log')

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_filename),
        logging.StreamHandler()
    ]
)

logging.info(f'Se extrae los datos de las empresas desdes wikipedia S&P500 desde Wiki')
df_sandp500=pd.read_html("https://es.wikipedia.org/wiki/Anexo:Compa%C3%B1%C3%ADas_del_S%26P_500")[0]
export_csv = df_sandp500.to_csv(r"empresasSp500.csv", index = None, header = True)
#listaSp500=pd.read_csv('C:\Bootcamp\AnalisisDeDatos\Componente_Tecnico\Proyecto\sp500.py')["Símbolo"].tolist()
df_listaSp500 = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]['Symbol'].tolist()

"""for df_listaSp500 in df_listaSp500:
    print(df_listaSp500)
"""
def extract_data(symbol, start_date, end_date):
    try:
        logging.info(f'Extrayendo datos para {symbol} desde {start_date} hasta {end_date}')
        data = yf.download(symbol, start=start_date, end=end_date)
        logging.info(f'Datos extraídos exitosamente para {symbol}')
        return data
    except Exception as e:
        logging.error(f'Error extrayendo datos para {symbol}: {e}')
        return None

def transform_data(data, symbol):
    try:
        logging.info('Transformando datos')
        df = data[['Close']].reset_index()
        df['ticker'] = symbol
        df.rename(columns={'Date': 'date', 'Close': 'close'}, inplace=True)
        df=df[['ticker', 'date', 'close']]
        logging.info('Datos transformados exitosamente')
        return df
    except Exception as e:
        logging.error(f'Error transformando datos: {e}')
        return None

def load_data(df):
    try:
        filename = os.path.join(data_dir, 'data_combinada.csv')
        logging.info(f'Guardando datos transformados en {filename}')
        df.to_csv(filename, index=False)
        logging.info('Datos guardados exitosamente')
    except Exception as e:
        logging.error(f'Error guardando datos: {e}')

def etl_process(symbol, start_date, end_date):
    data = extract_data(symbol, start_date, end_date)
    if data is not None:
        transformed_data = transform_data(data, symbol)
        if transformed_data is not None:
            return transformed_data
    return None


start_date = '2024-01-01'
end_date = '2024-03-31'
combined_data=pd.DataFrame()


for symbol in df_listaSp500:
    data = etl_process(symbol, start_date, end_date)
    if data is not None:
        combined_data = pd.concat([combined_data, data], ignore_index=True)

if not combined_data.empty:
    load_data(combined_data)
else:
    logging.warning('No se pudo obtener datos para ningún símbolo')