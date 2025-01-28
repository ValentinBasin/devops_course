variable "AWS_ACCESS_KEY" { type = string }
variable "AWS_SECRET_KEY" { type = string }
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
