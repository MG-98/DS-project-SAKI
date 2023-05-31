# Project Plan

## Summary

<!-- Describe your data science project in max. 5 sentences. -->
This project analyzes the location of free/open hotspots and road sections. In order to identify the streets and routes that have the suitable internet infrastructre for new services test. I will use Koln as use case. 

## Rationale

<!-- Outline the impact of the analysis, e.g. which pains it solves. -->
Getting the road sections that has the suitable interent infrastructre, will make it easier to choose the places where the new serives , ex. speed monitoring, traffic light smart atomation or any IOT application that is realted to samrt cities. This location will make it feasable to test the new technologies without the headace of making the whole infrastucture needed for it. 

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: Hotspots in Koeln
* Metadata URL: https://mobilithek.info/offers/-2520158348704562625
* Data URL: https://geoportal.stadt-koeln.de/arcgis/rest/services/politik_und_verwaltung/breitbandinfrastrukturkataster/MapServer/13/query?where=objectid%20is%20not%20null&text=&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&distance=&units=esriSRUnit_Foot&relationParam=&outFields=%2A&returnGeometry=true&returnTrueCurves=false&maxAllowableOffset=&geometryPrecision=&outSR=4326&havingClause=&returnIdsOnly=false&returnCountOnly=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&returnZ=false&returnM=false&gdbVersion=&historicMoment=&returnDistinctValues=false&resultOffset=&resultRecordCount=&returnExtentOnly=false&datumTransformation=&parameterValues=&rangeValues=&quantizationParameters=&featureEncoding=esriDefault&f=pjson
* Data Type: JSON

List of urban hotspots in Cologne. To be able to use the public hotspots, select "hotspot.koeln" in your Wi-Fi settings and register once on the home page. A map-based representation can be accessed here: http://www.stadt-koeln.de/basisdienste/wlan/.

### Datasource1: Strassenabschnitte Köln
* Metadata URL: https://mobilithek.info/offers/-7863335389674294899
* Data URL: https://geoportal.stadt-koeln.de/arcgis/rest/services/basiskarten/kgg_labeled/MapServer/9/query?where=objectid%20is%20not%20null&text=&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&distance=&units=esriSRUnit_Foot&relationParam=&outFields=%2A&returnGeometry=true&returnTrueCurves=false&maxAllowableOffset=&geometryPrecision=&outSR=4326&havingClause=&returnIdsOnly=false&returnCountOnly=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&returnZ=false&returnM=false&gdbVersion=&historicMoment=&returnDistinctValues=false&resultOffset=&resultRecordCount=&returnExtentOnly=false&datumTransformation=&parameterValues=&rangeValues=&quantizationParameters=&featureEncoding=esriDefault&f=pjson
* Data Type: JSON

The Cologne street directory provides an overview of all applicable street names and addresses.


## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->


1. Data exploration and analysis. #1[i1]
2. Make an automated data pipeline. #2[i2]
3. Use clustering techniques for finding the related hotspot locations.#3[i3]
4. Find connected streets to build routes.#4[i4]
5. Build automated testing.#5[i5]
6. Continuous integration.#6[i6]




[i1]: https://github.com/MG-98/DS-project-SAKI/issues/1
[i2]: https://github.com/MG-98/DS-project-SAKI/issues/2
[i3]: https://github.com/MG-98/DS-project-SAKI/issues/3
[i4]: https://github.com/MG-98/DS-project-SAKI/issues/4
[i5]: https://github.com/MG-98/DS-project-SAKI/issues/5
[i6]: https://github.com/MG-98/DS-project-SAKI/issues/6
