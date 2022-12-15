
terraform {

  backend "s3" {
    bucket         = "cits-tfstate"
    key            = "cits-tfstate.tfstate"
    encrypt        = false
    dynamodb_table = "cits-tfstate-lock"
  }
}

resource "aws_s3_bucket" "sagemaker_2" {
  bucket = "cits-sagemaker-2"
  tags = {
    Name        = "sagemaker_2"
    Environment = "Dev"
  }
}

resource "aws_s3_object" "object" {
  bucket = aws_s3_bucket.sagemaker_2.id
  key    = "sagemaker_2.model"
  source = "../hello_world/readme.md"
  etag = filemd5("../hello_world/readme.md")
}
