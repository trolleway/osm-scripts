import os
import psycopg2

'''
generate milestones for single line in geojson file, using PostGIS. 
input: 	source.json
output:	route.gpx with route for garmin
	View public.milestones in PostGIS database with points 

'''

def process():
	dbname='residential'
	user='user'
	host='localhost'
	password='user'
	try:
		conn = psycopg2.connect("dbname='" + dbname + "' user='"
                                + user + "' host='" + host
                                + "' password='" + password + "'")
	except:
		print 'I am unable to connect to the database'
		return 0
	cur = conn.cursor()
	sql ='''
	DROP TABLE IF EXISTS pkline;

	
	'''

	cur.execute(sql)
	conn.commit()


	os.system('''
	ogr2ogr -overwrite -f "PostgreSQL" PG:"host=localhost user=user dbname=residential password=user"  -nln pkline source.json -s_srs EPSG:4326 -t_srs EPSG:32637
	''')

	os.system('''
	rm route.gpx -f
	''')
	os.system('''
	ogr2ogr -overwrite -f "GPX" route.gpx   source.json -s_srs EPSG:4326 -select name -dsco FORCE_GPX_ROUTE=YES
	''')

	cur = conn.cursor()
	sql ='''
	CREATE OR REPLACE VIEW milestones AS
	(
	-- calculate lenght of line
	WITH line_length as (SELECT round((ST_Length(wkb_geometry)/1000)::numeric,3) AS line_length FROM pkline )
	-- calculate record id
	SELECT wkb_geometry, (row_number() OVER ()) AS id FROM 
	(SELECT 
	st_line_interpolate_point
		(wkb_geometry, 
		generate_series
			(0,
			(line_length.line_length*100)::integer,
			1*100)
		/(line_length.line_length*100)::real) 
		AS wkb_geometry
	 FROM line_length, pkline) AS points_calculation
	);

	
	'''


	




if __name__ == '__main__':
	process()
