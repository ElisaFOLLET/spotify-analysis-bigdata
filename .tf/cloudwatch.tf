resource "aws_cloudwatch_event_rule" "every_day" {
  name = "every-day"
  description = "Sends a trigger every day"
  schedule_expression = "rate(1 minute)"
  is_enabled = false
}

resource "aws_cloudwatch_event_target" "trigger_cmo_strategy" {
  rule = "${aws_cloudwatch_event_rule.every_day.name}"
  target_id = "spotify_analysis"
  arn = "${aws_lambda_function.spotify_analysis.arn}"
}
