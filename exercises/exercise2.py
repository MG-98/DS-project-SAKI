import pandas as pd
import sqlite3

######################### Data Extraction ##########################

trainstops_csv = 'https://download-data.deutschebahn.com/static/datasets/haltestellen/D_Bahnhof_2020_alle.CSV'
trainstops_df = pd.read_csv(trainstops_csv , sep=';' )

######################### Data Transformation #######################

# drop the "Status" column
trainstops_df.drop(columns=['Status'] , inplace=True)

# Valid "Verkehr" values are "FV", "RV", "nur DPN"
trainstops_df = trainstops_df[trainstops_df['Verkehr'].isin(["FV", "RV", "nur DPN"])]

# Valid "Laenge", "Breite" values are geographic coordinate system values between -90 and 90
trainstops_df['Breite'] = trainstops_df['Breite'].map(lambda x: float(x.replace(',' , '.')))
trainstops_df = trainstops_df[(trainstops_df['Breite']>-90) & (trainstops_df['Breite']<90)]

trainstops_df['Laenge'] = trainstops_df['Laenge'].map(lambda x: float(x.replace(',' , '.')))
trainstops_df = trainstops_df[(trainstops_df['Laenge']>-90) & (trainstops_df['Laenge']<90)]

# Empty cells are considered invalid
trainstops_df = trainstops_df.dropna()

#Valid "IFOPT" values follow this pattern:
#<exactly two characters>:<any amount of numbers>:<any amount of numbers><optionally another colon followed by any amount of numbers>
mask = trainstops_df['IFOPT'].str.match("[a-zA-Z][a-zA-Z]:\d+:[\d|\d:\d]+")
trainstops_df = trainstops_df[mask]

############################ Data Loading ##############################

conn = sqlite3.connect('trainstops.sqlite')
trainstops_df.to_sql('trainstops',conn,if_exists='replace',index=False)
conn.commit()
conn.close() 