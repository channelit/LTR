terraform {
  backend "s3" {
    bucket         = "cits-tfstate"
    key            = "cits-tfstate.tfstate"
    encrypt        = false
    dynamodb_table = "cits-tfstate-lock"
  }
}
resource "aws_s3_bucket" "cits-tfstate" {
  bucket = "cits-tfstate"
  tags = {
    Name        = "cits-tfstate"
    Environment = "Dev"
  }
}
