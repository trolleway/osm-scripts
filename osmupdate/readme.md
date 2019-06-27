
run
```
docker build  https://raw.githubusercontent.com/trolleway/osm-scripts/master/osmupdate/Dockerfile --no-cache --tag osmupdate
docker volume create osmupdate_data
#mount with volume for production
docker run -it  \
  --name osmupdate \
  --mount type=volume,source=osmupdate_data,target=/data \
  osmupdate
  

```
