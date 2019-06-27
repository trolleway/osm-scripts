
run
```
docker build  https://raw.githubusercontent.com/trolleway/osm-scripts/master/osmupdate/Dockerfile --no-cache --tag osmupdate

#work using bind 
docker volume create osmupdate_data
docker run -it  \
  --rm \
  --name osmupdate \
  --mount type=bind,source=$(pwd)/osmupdate_data,target=/data \
  osmupdate
  
  
  

```
