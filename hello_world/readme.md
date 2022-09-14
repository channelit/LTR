#### Run docker locally
```
docker run -v $(pwd)/hello-world-model.pkl:/opt/ml/model/hello-world-model.pkl -p 5001:8080 --name=local cits_byo:m1 serve

```