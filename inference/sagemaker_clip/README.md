

#### Build run locally
```shell
docker buildx build --platform=linux/arm64 -t local:m1 .
docker run -v $(pwd)/model.pkl:/opt/ml/model.pkl -p 5001:8000 --name=local local:m1 serve
```