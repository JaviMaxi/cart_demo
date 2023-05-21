echo $1
docker container run -v cart_demo_media:/run/media -v $(pwd)/backups:/backups alpine:latest tar -zxvf $1 . -C /run/