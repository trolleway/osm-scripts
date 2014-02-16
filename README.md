osm-scripts
===========
landuse_by_buffers - скрипт для облегчения рисования кварталов landuse=residential. Генерирует полигоны, границами которых являются буферные зоны улиц.

### Описание
Скрипт читает файл geojson, в котором находится геометрия автодорог какого-нибудь райцентра. Вызывает ogr2ogr, который грузит его в PostGIS. PostGIS создаёт выпуклую оболочку (convex hull) вокруг города, и вырезает из неё буферные зоны  дорог. Потом экспортирует получившийся полигон с щелями в формат osm, вызывая утилиту ogr2osm.
В файле получаются замкнутые полигоны, которые выглядят как кварталы.
Пользователь открывает получившийся файл в JOSM, и берёт из него нужные обьекты, вешает теги, и грузит в базу OSM, предварительно их подрезав и подправив.

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

### Использование

1. Загрузите в JOSM какой-нибудь райцентр, где вы хотите нарисовать landuse=residential
2. Выберите фильтром линии (улицы + границы города + природа(?)), вокруг которых будут строится буфера. Создайте два фильтра: 
```
trunk|motorway|primary|secondary|tertiary|unclassified|residential|track|railway|natural|living_street|waterway|place
```
```
type:node
```
3. Скопируйте дороги, вокруг которых будут строится буфера в отдельный слой JOSM
