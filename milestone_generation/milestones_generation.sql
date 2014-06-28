-- Generate milstones / kilometer points for single line
-- wtfpl by trolleway
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
 FROM line_length, pkline) AS points_calculation;
