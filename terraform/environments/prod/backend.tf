terraform {
  backend "gcs" {
    prefix = "env/warehouse"
    bucket = "dec-cam-dec-cam-dev-tf-c5f6"
  }
}
