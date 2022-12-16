resource "aws_ecr_repository" "sagemaker-search" {
  name                 = "sagemaker-search"
  image_tag_mutability = "MUTABLE"
}

resource "docker_registry_image" "sagemaker-search" {
  name = "122936777114.dkr.ecr.us-east-1.amazonaws.com/cits_byo:latest"
  build {
    context = "../inference/sagemaker_clip"
    dockerfile = "Dockerfile"
  }
}