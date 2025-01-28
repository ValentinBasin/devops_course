provider "aws" {
  region = var.region
}
terraform {
  backend "s3" {
    bucket = "bvm-test-bucket" # should already be exists as this part happens as part of the init process and not the apply
    key    = "terraform/myproject"
    region = "il-central-1"
  }
}
