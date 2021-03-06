 resource "aws_cloudwatch_event_rule" "backup_snapshot_reion_cron" {
     name = "backup_snapshot_region"
     description = "Make backup of snapshot to us-east-2"
     schedule_expression = "rate(4 minutes)"
 }
 resource "aws_cloudwatch_event_target" "copy_to_region" {
     rule = aws_cloudwatch_event_rule.backup_snapshot_reion_cron.name
     target_id = "copy-us-east-1"
     arn = aws_lambda_function.lambda_copy_to_region.arn
 }
 resource "aws_lambda_permission" "allow_cloudwatch_to_call_check_foo" {
     statement_id = "AllowExecutionFromCloudWatch"
     action = "lambda:InvokeFunction"
     function_name = aws_lambda_function.lambda_copy_to_region.function_name # Define your Lambda Function
     principal = "events.amazonaws.com"
     source_arn = aws_cloudwatch_event_rule.backup_snapshot_reion_cron.arn
 }






# # ==================  Event Based Rules ==========================
# resource "aws_cloudwatch_event_rule" "event_based_triggering" {
#     name = "Start_the_instance_based_on_condition"
#     description = "Fires every one minutes"
#     event_pattern  = <<EOF
# {
#   "source": ["aws.ec2"],
#   "detail-type": ["EC2 Instance State-change Notification"],
#   "detail": {
#     "state": ["running"]
#   }
# }
# EOF

# # =================== Event Based Target ==============================
# resource "aws_cloudwatch_event_target" "based_on_event" {
#     rule = aws_cloudwatch_event_rule.event_based_triggering.name
#     target_id = "check_foo"
#     arn = aws_lambda_function.lambda.arn

# # ================== Lambda Permission ================================
# resource "aws_lambda_permission" "allow_cloudwatch_to_call_check_foo" {
#     statement_id = "AllowExecutionFromCloudWatch"
#     action = "lambda:InvokeFunction"
#     function_name = aws_lambda_function.lambda.function_name # Define your Lambda Function
#     principal = "events.amazonaws.com"
#     source_arn = aws_cloudwatch_event_rule.event_based_triggering.arn
# }