resource "aws_instance" "example" {
  ami           = var.AMIS[var.region]
  instance_type = "t3.micro"
}

resource "aws_instance" "new_instance" {
  ami           = var.AMIS[var.region]
  instance_type = "t3.micro"
}
