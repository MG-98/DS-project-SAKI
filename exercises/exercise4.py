from zipfile import ZipFile
import urllib.request
import pandas as pd
import sqlite3

# loading the zip file
dataset_zip_url = 'https://www.mowesta.com/data/measure/mowesta-dataset-20221107.zip'
_, _ = urllib.request.urlretrieve(dataset_zip_url , filename='dataset.zip')

# specifying the zip file name
file_name = "dataset.zip"
  
# opening the zip file in READ mode
with ZipFile(file_name, 'r') as zip:
    # extracting all the files
    zip.extractall()

temperature_df  = pd.read_csv('data.csv' , sep=';' , header=None, names=range(500))

################################# Data preperation ##################################
# handling extra fields
temperature_df.columns = temperature_df.iloc[0]
temperature_df  = temperature_df[1:]
temperature_df = temperature_df.iloc[:, 0:11]
temperature_df = temperature_df[['Geraet' , 'Hersteller' ,'Model' ,'Monat' ,'Temperatur in °C (DWD)' , 'Batterietemperatur in °C' , 'Geraet aktiv']]

# renaming coloums
temperature_df = temperature_df.rename(columns={"Temperatur in °C (DWD)": "Temperatur", "Batterietemperatur in °C": "Batterietemperatur"})

# converting datatypes
temperature_df['Temperatur'] = temperature_df['Temperatur'].map(lambda x: float(x.replace(',' , '.')))
temperature_df['Batterietemperatur'] = temperature_df['Batterietemperatur'].map(lambda x: float(x.replace(',' , '.')))
temperature_df = temperature_df.astype({'Geraet': 'int64' , 'Monat' : 'int64' ,  'Temperatur' : 'float64' , 'Batterietemperatur' : 'float64' })

################################# Data transofrmation ################################
temperature_df['Temperatur'] = (temperature_df['Temperatur']*9/5) +32 
temperature_df['Batterietemperatur'] = (temperature_df['Batterietemperatur']*9/5) +32 

################################# Data validation ####################################
temperature_df = temperature_df.dropna()
temperature_df = temperature_df[temperature_df['Geraet'] > 0]

################################# Data loading ####################################
conn = sqlite3.connect('temperatures.sqlite')
temperature_df.to_sql('temperatures',conn,if_exists='replace',index=False)