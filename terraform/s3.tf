
resource "aws_s3_bucket" "sagemaker_2" {
  bucket = "cits-sagemaker-2"
  tags = {
    Name        = "sagemaker_2"
    Environment = "Dev"
  }
}

resource "aws_s3_object" "object" {
  bucket = aws_s3_bucket.sagemaker_2.id
  key    = "model.pkl"
  source = "../inference/sagemaker_clip/sample.pkl"
  etag = filemd5("../inference/sagemaker_clip/sample.pkl")
}
