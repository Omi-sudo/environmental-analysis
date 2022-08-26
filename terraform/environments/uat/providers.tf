terraform {
  required_providers {
    google = {
      version = "~>4.0"
    }
  }
}

provider "google" {
  project = var.project_id
}

data "google_client_config" "access_token" {}
