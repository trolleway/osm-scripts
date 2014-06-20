'''
ogr2ogr -f "PostgreSQL" PG:"host=localhost user=user dbname=osmdb3 password=user" export.geojson -nln lines -nlt LINESTRING -OVERWRITE -t_srs "EPSG:3857" -lco OVERWRITE=YES -progress 
'''
