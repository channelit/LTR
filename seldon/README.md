##### Venv Commands
```
python -m venv venv
source venv/bin/activate
pip freeze > requirements.txt
pip install -r requirements.txt
```


#### Build Image
```
docker buildx create --use
docker buildx build --push --platform linux/amd64,linux/arm64 . -t channelit/reco:0.1
```