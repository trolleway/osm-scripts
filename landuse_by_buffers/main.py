import os
import psycopg2
import config

#Take an roads.geojson, and make a many polygons beetwen roads in osm format.
#Open OSM file in JOSM, and you get a fancy medium-zoom landuse map


def process(ConnectionString):
	try:
		conn = psycopg2.connect(ConnectionString)
	except:
		print 'I am unable to connect to the database'
		return 0
	cur = conn.cursor()
	sql ='''
	DROP TABLE IF EXISTS roads;
	DROP TABLE IF EXISTS areas;
	DROP TABLE IF EXISTS areas_singlegeom;
	
	'''

	cur.execute(sql)
	conn.commit()


	os.system('''
	ogr2ogr -overwrite -f "PostgreSQL" PG:"'''+ConnectionString+'''"  -nln roads roads.geojson -s_srs EPSG:4326 -t_srs EPSG:3857
	''')

	sql='''
	CREATE TABLE areas AS
		SELECT 
		1 AS id,	
		ST_Difference(
			ST_ConvexHull(ST_Collect(wkb_geometry)),
			ST_Buffer(ST_Collect(wkb_geometry),10)
			)
			AS poly
		FROM roads;

	CREATE TABLE areas_singlegeom AS
		SELECT
		ST_GeometryN(poly,generate_series(1,ST_NumGeometries(poly))) AS geom,
		'residential' AS landuse,
		'highway buffers' AS source
		FROM areas;
	'''
	cur.execute(sql)
	conn.commit()

	os.system('''
	mkdir temp
	''')

	os.system('''
	ogr2ogr -overwrite temp PG:"'''+ConnectionString+'''"  "areas_singlegeom" -nlt MULTIPOLYGON -s_srs EPSG:3857 -t_srs EPSG:4326
	''')

	os.system('''
	rm areas_singlegeom.osm
	''')

	os.system('''
python ogr2osm/ogr2osm.py temp/areas_singlegeom.shp
	''')
		
	os.system('''
	rmdir temp
	''')

if __name__ == '__main__':
	process("dbname='" + config.dbname + "' user='"
                                + config.user + "' host='" + config.host
                                + "' password='" + config.password + "'")
