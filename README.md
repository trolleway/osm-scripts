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
3. Выледите рамкой линии, и скопируйте их в отдельный слой JOSM
4. Сохраните новый слой как osm-scripts/landuse_by_bufers/roads.geojson
5. python osm-scripts/landuse_by_bufers/main.py
6. Откройте получившийся areas.osm в JOSM
7. Удалите из него Relation. Упростите кварталы коммандой Shift+Y, а то кто-нибудь докопается. 
8. Повесьте теги (не забывайте про фильтр type:node)
9. Скачайте данные по городу в отдельный слой, и копируйте из roads.osm в новый слой квартальчики. 
10. Включите подложку bing, и проверяйте, что у вас получилось
