output "ec2_public_ip_dev" {
    value = aws_instance.lambda_test_instances.public_ip
}

output "ec2_public_ip_prod" {
    value = aws_instance.lambda_test_instances_2.public_ip
}

output "ec2_name_prod" {
    value = aws_instance.lambda_test_instances_2.ami
}

output "ec2_name_dev" {
    value = aws_instance.lambda_test_instances.ami
}