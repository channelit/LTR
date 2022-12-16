
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
  source = "../inference/sagemaker_clip/model.pkl"
  etag = filemd5("../inference/sagemaker_clip/model.pkl")
}
