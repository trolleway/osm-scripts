osm-scripts
===========
landuse_by_buffers - скрипт для облегчения рисования кварталов landuse=residential. Генерирует полигоны, границами которых являются буферные зоны улиц.

### Зависимости
PostGIS
ogr2ogr
ogr2osm

### Установка
1. Создать БД:
```
createdb residential
psql -d residential
CREATE EXTENSION postgis;
\q
```
2. git clone https://github.com/trolleway/osm-scripts.git
3. cd osm-scripts/landuse_by_bufers
4. git clone --recursive https://github.com/pnorman/ogr2osm
