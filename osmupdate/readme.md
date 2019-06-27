
run
```
sudo docker build  https://raw.githubusercontent.com/trolleway/osm-scripts/master/osmupdate/Dockerfile --no-cache --tag osmupdate
mkdir -p "$(pwd)"/osmupdate_data

#work using bind 
mkdir osmupdate_data

sudo docker run -it  \
  --rm \
  --name osmupdate \
  --mount type=bind,source="$(pwd)"/osmupdate_data,target=/data \
  osmupdate
  
  
  

```
