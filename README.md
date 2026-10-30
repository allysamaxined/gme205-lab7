# Programming Exercise 7
## Python-PostGIS to Interoperable GeoJSON

### Introduction to the Programming Exercise
This programming exercise focuses on connecting Python to the Lab 6 PostGIS database, retrieve the selected parcelrows with a parameterized query, convert rows into Parcel objects, and export a validated GeoJSON FeatureCollection. 

To complete this laboratory exercise, one needs to have the Laboratory Exercise 6 completed. It will be used as a schema, specifically the parcels, buildings, and roads.

### Materials/Tools
1. Python
2. VSCode
3. PostgreSQL/PostGIS
4. pgAdmin Query Tool
5. psycopg 3
6. python-dotenv
7. JSON

### Project Structure
gme205-lab7/ 
├── output/ 
│   
└── residential_parcels.geojson 
├── src/ 
│   
├── database.py 
│   
├── spatial.py 
│   
├── exchange.py 
│   
└── run_lab7.py 
├── .env 
├── .env.example 
├── .gitignore 
├── README.md 
└── requirements.txt

#### Part F.1 – Data Path

**1. What responsibility belongs to PostgreSQL/PostGIS in this workflow?**

The responsibility of PostgreSQL/PostGIS in this workflow is to store and manage the spatial data used by the program. PostgreSQL allows the parcel information to persist, while PostGIS provides the functions needed to handle the spatial geometries. By using both, I'm able to retrieve the required parcel information from the database, including its land_use classification and geometry, even after the program itself stops.

**2. Why is land_use passed as a query parameter instead of inserted into the SQL string?**

The land_use attribute is passed as a query parameter instead of directly inserting it into the SQL string because it allows the query and its values to be handled separately. By doing this, I'm able to change the land_use classification being searched without having to modify the SQL statement itself. It also helps prevent SQL injection, since the supplied value is treated as data rather than part of the SQL command.

**3. What changes when a database row becomes a Parcel object?**

When a database row becomes a Parcel object, the information retrieved from PostgreSQL is converted into a Python object. Instead of accessing the information through its position in the database row, I'm now able to access it through the Parcel object's attributes, such as parcel_id, land_use, and geometry. By doing this, the parcel information becomes easier to organize and use within the object-oriented structure of the program.

**4. What changes when a Parcel object becomes a GeoJSON Feature?**

When a Parcel object becomes a GeoJSON Feature, its information is converted into a format that can be understood by other GIS applications. The parcel_id becomes the feature's identifier, while the land_use and parcel_id are included in its properties. Its geometry is also included as part of the GeoJSON Feature. By converting it this way, I'm able to export the parcel information without requiring another application to understand how the Python Parcel class works.

**5. Why is ST_Transform(..., 4326) placed at the exchange boundary?**

The ST_Transform(..., 4326) function is placed at the exchange boundary because the stored parcel geometries use EPSG:32651, while the GeoJSON output requires coordinates using EPSG:4326. Instead of changing the original geometry stored in the database, the transformation is performed when the data is being retrieved for export. By doing this, I'm able to preserve the original spatial data while making sure that the exported GeoJSON uses the appropriate coordinate reference system.

**6. Why is producing a valid GeoJSON file an interoperability exercise even though you did not build an API?**

Producing a valid GeoJSON file is considered an interoperability exercise because it allows spatial data from one system to be used by another application. Even though I did not create an API, the GeoJSON file still serves as a way of exchanging information between different systems. For example, the parcel information originally stored in PostgreSQL/PostGIS can be exported through Python and opened in QGIS. By doing this, I'm able to demonstrate that the spatial data can be shared and understood by another application without requiring it to use the same database or Python code.