#### Build and push to AWS Private Docker Registry (created using console)
```
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 122936777114.dkr.ecr.us-east-1.amazonaws.com
-- Normal build
docker build  --platform=linux/amd64 -t cits_byo . 
-- Command below for linux platform that WORKS
docker build --platform=linux/amd64 -t cits_byo . 
-- Command below is for multiplatform -- THIS WILL CREATE AN INDEX NOT VALID FOR CREATING MODEL
docker buildx build --push --platform linux/amd64,linux/arm64 -t 122936777114.dkr.ecr.us-east-1.amazonaws.com/cits_byo . 

-- Tage Image
docker tag cits_byo 122936777114.dkr.ecr.us-east-1.amazonaws.com/cits_byo
docker push 122936777114.dkr.ecr.us-east-1.amazonaws.com/cits_byo
```


#### Inference using AWS CLI
```
aws sagemaker-runtime invoke-endpoint --endpoint-name 'byo' --body fileb://hello_world.csv --content-type=text/csv output_file.txt
```
