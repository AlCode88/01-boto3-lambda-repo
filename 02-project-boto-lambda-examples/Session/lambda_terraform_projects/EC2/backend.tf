terraform {
  backend "s3" {
    bucket = "terraform-bucket-tb"
    key = "Resources/test_instance.tfstate"
    region = "us-east-1"
  }
}
