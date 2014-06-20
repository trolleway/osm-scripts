-- Разбивка линий на сегменты
-- Проверено на типе LINESTRING

DROP VIEW IF EXISTS sunlines_all;
CREATE OR REPLACE VIEW sunlines_all AS
SELECT (ST_MakeLine(start_point,end_point)) as wkb_geometry, row_number() OVER () AS id,
degrees(ST_Azimuth(start_point,end_point)) AS azimuth
  FROM
(
    SELECT 
        ST_Pointn(wkb_geometry, generate_series(1, ST_NumPoints(wkb_geometry)-1)) as start_point, 
        ST_Pointn(wkb_geometry, generate_series(2, ST_NumPoints(wkb_geometry))) as end_point
    FROM (
        SELECT  wkb_geometry FROM lines
        ) as line
) as tmp;       
    
DROP VIEW IF EXISTS sunlines_1000;
CREATE OR REPLACE VIEW sunlines_1000 AS
SELECT * 
FROM sunlines_all
WHERE
azimuth BETWEEN 90 AND 105;

DROP VIEW IF EXISTS sunlines_1300;
CREATE OR REPLACE VIEW sunlines_1300 AS
SELECT * 
FROM sunlines_all
WHERE
azimuth BETWEEN 160 AND 170;

DROP VIEW IF EXISTS sunlines_1500;
CREATE OR REPLACE VIEW sunlines_1500 AS
SELECT * 
FROM sunlines_all
WHERE
azimuth BETWEEN 180 AND 190;

DROP VIEW IF EXISTS sunlines_1900;
CREATE OR REPLACE VIEW sunlines_1900 AS
SELECT * 
FROM sunlines_all
WHERE
azimuth BETWEEN 260 AND 270;
