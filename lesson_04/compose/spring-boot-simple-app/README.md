Deploy local docker registry:

docker run -d  -p 5000:5000 --restart=always --name registry  -v /mnt/registry:/var/lib/registry  registry:2