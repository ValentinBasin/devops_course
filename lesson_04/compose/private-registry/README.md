# Running a private registry

## **Problem:** *Using the public Docker Hub is easy. However, you might have data governance con‐cerns with your images being hosted outside your own infrastructure. Therefore, you would like to run your own Docker registry, hosting it on your own infrastructure.*

### Run + Push image to private repository
```
docker pull registry:2
docker run -d -p 8082:5000 registry:2

curl -i http://localhost:8082/v2/

docker tag hello-flask localhost:8082/hello-flask
docker push localhost:8082/hello-flask

curl http://localhost:8082/v2/_catalog
```