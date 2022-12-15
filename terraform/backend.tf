terraform {
  backend "s3" {
    bucket         = "cits-tfstate"
    key            = "state/terraform.tfstate"
    encrypt        = false
    dynamodb_table = "cits-tfstate"
  }
}
resource "aws_s3_bucket" "cits-tfstate" {
  bucket = "cits-tfstate"
  tags = {
    Name        = "cits-tfstate"
    Environment = "Dev"
  }
}
resource "aws_s3_bucket_public_access_block" "block" {
 bucket = aws_s3_bucket.cits-tfstate.id

 block_public_acls       = true
 block_public_policy     = true
 ignore_public_acls      = true
 restrict_public_buckets = true
}
resource "aws_dynamodb_table" "cits-tfstate" {
 name           = "cits-tfstate"
 read_capacity  = 20
 write_capacity = 20
 hash_key       = "LockID"

 attribute {
   name = "LockID"
   type = "S"
 }
}