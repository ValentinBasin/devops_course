resource "aws_instance" "ec2_01" {
  ami           = var.AMIS[var.region]
  instance_type = var.instanceType
}

resource "aws_instance" "ec2_02" {
  ami           = var.AMIS[var.region]
  instance_type = var.instanceType
}

resource "aws_s3_bucket" "s3_01" {
  bucket = "bvm-test-bucket-12344321"
}
