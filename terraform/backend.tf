terraform {
  backend "s3" {
    bucket         = "cits-tfstate"
    key            = "cits-tfstate.tfstate"
    encrypt        = false
    dynamodb_table = "cits-tfstate-lock"
  }
}