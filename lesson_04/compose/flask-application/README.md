# Packaging a Flask App

## **Problem**: *web application built with the Python framework Flask, running in Ubuntu 14.04.*

### Build + Run
```
docker build . -t hello-flask
docker run -itd -p 80:5000 hello-flask
```

### Access you app
```
http://<vagrant machine IP>/hi
```