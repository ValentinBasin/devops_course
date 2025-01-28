variable "region" {
  type    = string
  default = "il-central-1"
}
variable "AMIS" {
  type = map(string)
  default = {
    "il-central-1" = "ami-03cb6cd40ab8a015f"
  }
}
variable "instanceType" {
  type    = string
  default = "t3.micro"
}
