resource "aws_instance" "ec2_01" {
  ami           = var.AMIS[var.region]
  instance_type = var.instanceType
  provisioner "local-exec" {
    command = "echo ${aws_instance.ec2_01.public_dns} > dns.txt"
  }
  key_name                    = "bvm-mac"
  associate_public_ip_address = true
}

resource "aws_s3_bucket" "s3_01" {
  bucket = "bvm-test-bucket-12344321"
}
