resource "aws_instance" "lambda_test_instances" {
  ami                     = data.aws_ami.Amazon_linux_2.id
  instance_type           = var.instance_type
  vpc_security_group_ids = [aws_security_group.session3_SG.id]
  user_data               = file("userdata.sh")
  root_block_device {
    volume_size           = "8"
    volume_type           = "gp2"
    encrypted             = true
    delete_on_termination = true
  }


  tags = {
    Name = var.project_name
    env = var.env_dev
  }
  volume_tags = {
    Name = var.project_name
    env = var.env_dev
  }
}

resource "aws_instance" "lambda_test_instances_2" {
  ami                     = data.aws_ami.Amazon_linux_2.id
  instance_type           = var.instance_type
  vpc_security_group_ids = [aws_security_group.session3_SG.id]
  user_data               = file("userdata.sh")
  root_block_device {
    volume_size           = "8"
    volume_type           = "gp2"
    encrypted             = true
    delete_on_termination = true
  }

  tags = {
    Name = var.project_name
    env = var.env_prod
  }

  volume_tags = {
    Name = var.project_name
    env = var.env_prod
  }
}