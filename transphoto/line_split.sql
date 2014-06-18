-- Разбивка линий на сегменты
-- Проверено на типе LINESTRING

SELECT (ST_MakeLine(start_point,end_point)) as geom, row_number() OVER () AS id,
round(degrees(ST_Azimuth(start_point,end_point))) AS azimuth
  FROM
(
    SELECT 
        ST_Pointn(geom, generate_series(1, ST_NumPoints(geom)-1)) as start_point, 
        ST_Pointn(geom, generate_series(2, ST_NumPoints(geom))) as end_point
    FROM (
        SELECT  geom FROM lines
        ) as line
) as tmp;   
