#### Build and push to AWS Private Docker Registry (created using console)
```
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 122936777114.dkr.ecr.us-east-1.amazonaws.com
-- Normal build
docker build  --platform=linux/amd64 -t cits_byotf . 
-- Command below  is not tried but should work
docker build  --platform=linux/amd64 -t cits_byotf . 
-- Command below is for multiplatform -- THIS WORKS
docker buildx build --push --platform linux/amd64,linux/arm64 -t 122936777114.dkr.ecr.us-east-1.amazonaws.com/cits_byotf . 
```