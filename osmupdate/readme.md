
run
```
docker build  github.com/trolleway/openimagerynetwork-download --no-cache --tag oadm
docker volume create osmupdate_data
#mount with volume for production
docker run -it  \
  --name osmupdate \
  --mount type=volume,source=osmupdate_data,target=/data \
  oadm
  

```
