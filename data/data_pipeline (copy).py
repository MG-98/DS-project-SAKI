import urllib.request 
import json
import pandas as pd 
import psycopg2
import sqlite3
import numpy as np


def data_extractor_from_url(url):
    with urllib.request.urlopen(url) as url:
        data = json.load(url)
    return data

if __name__ == '__main__':
    
    ### Data links ###
    hotspots_in_koeln_data_url = ' https://geoportal.stadt-koeln.de/arcgis/rest/services/politik_und_verwaltung/breitbandinfrastrukturkataster/MapServer/13/query?where=objectid%20is%20not%20null&text=&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&distance=&units=esriSRUnit_Foot&relationParam=&outFields=%2A&returnGeometry=true&returnTrueCurves=false&maxAllowableOffset=&geometryPrecision=&outSR=4326&havingClause=&returnIdsOnly=false&returnCountOnly=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&returnZ=false&returnM=false&gdbVersion=&historicMoment=&returnDistinctValues=false&resultOffset=&resultRecordCount=&returnExtentOnly=false&datumTransformation=&parameterValues=&rangeValues=&quantizationParameters=&featureEncoding=esriDefault&f=pjson'
    road_sections_data_url = 'https://geoportal.stadt-koeln.de/arcgis/rest/services/basiskarten/kgg_labeled/MapServer/9/query?where=objectid%20is%20not%20null&text=&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&distance=&units=esriSRUnit_Foot&relationParam=&outFields=%2A&returnGeometry=true&returnTrueCurves=false&maxAllowableOffset=&geometryPrecision=&outSR=4326&havingClause=&returnIdsOnly=false&returnCountOnly=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&returnZ=false&returnM=false&gdbVersion=&historicMoment=&returnDistinctValues=false&resultOffset=&resultRecordCount=&returnExtentOnly=false&datumTransformation=&parameterValues=&rangeValues=&quantizationParameters=&featureEncoding=esriDefault&f=pjson'

    ### Data Extraction ###
    hotspots_in_koeln_data = data_extractor_from_url(hotspots_in_koeln_data_url)
    road_sections_data = data_extractor_from_url(road_sections_data_url)

    print("Data Extraction done sucessfully ....")

    ### Data Transformation ###

    hotspots_in_koeln_DF = pd.json_normalize(hotspots_in_koeln_data['features']) 
    hotspots_in_koeln_DF.rename(columns={'attributes.objectid': 'OBJECTID', 'attributes.stadtbezirk': 'Stadtbezirk' , 'attributes.ap_name':'AP Name' ,  'attributes.strassenname':'Straßenname' ,
    'attributes.haus_nr': 'Haus Nr' , 'attributes.auftragsstatus_gesamt' :'Auftragsstatus Gesamt' , 'geometry.x' :'Geometry_x' , 'geometry.y':'Geometry_y' }, inplace=True)

    road_sections_DF = pd.json_normalize(road_sections_data['features']) 
    road_sections_DF.rename(columns={'attributes.objectid': 'OBJECTID', 'attributes.nummer': 'Nummer' , 'attributes.strasse':'Straße' ,  'attributes.hsnr_von_links':'Hausnummer von links' ,
    'attributes.hsnr_bis_links': 'Hausnummer bis links' , 'attributes.hsnr_von_rechts' :'Hausnummer von rechts' ,'attributes.hsnr_bis_rechts' :'Hausnummer bis rechts' ,
    'attributes.laenge': 'Länge (m)' ,'attributes.globalid': 'GLOBALID' , 'attributes.st_length(shape)': 'st_length(shape)' , 'geometry.paths' :'Geometry_paths'  }, inplace=True)

    for i , r in enumerate(road_sections_DF['Geometry_paths']):
    # sqlite doesn't accept the list of lists as a type so , i put it in string and i will convert it back to list while processing
        road_sections_DF['Geometry_paths'][i] = str(r[0]) 
    
    print("Data Transformation done sucessfully ....")

    ### Data Loading ###

    conn = sqlite3.connect('project.sqlite')

    road_sections_DF.to_sql('road_sections',conn,if_exists='replace',index=False)
    hotspots_in_koeln_DF.to_sql('hotspots_in_koeln',conn,if_exists='replace',index=False)

    conn.commit()
    conn.close() 
    
    print("Data Loading done sucessfully ....")
