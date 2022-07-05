terraform {
  required_version = "~> 1.0"
  required_providers {
    aws = {
      version = "3.35.0"
      source  = "hashicorp/aws"
    }
  }
}