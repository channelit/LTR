resource "aws_ecr_repository" "sagemaker-search" {
  name                 = "sagemaker-search"
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }
}

resource "docker_registry_image" "helloworld" {
  name = "${aws_ecr_repository.sagemaker-search.repository_url}:latest"
  build {
    context = "../inference/sagemaker_clip"
    dockerfile = "Dockerfile"
  }
}