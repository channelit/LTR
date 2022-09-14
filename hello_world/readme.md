#### Run docker locally
```
docker run -v $(pwd)/model.pkl:/opt/ml/model/model.pkl -p 5001:8080 --name=local cits_byo:m1 serve
```