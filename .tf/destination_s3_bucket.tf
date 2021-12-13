# Create a S3 bucket - destination of the data pipeline
resource "aws_s3_bucket" "analytics_destination" {
  bucket = "spotify-analysis-data-1"
  acl    = "private"
}
