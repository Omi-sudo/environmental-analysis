variable "project_id" {
  type        = string
  description = "GCP Project ID"
  default     = "dec-cam-u-warehouse-9057"

  validation {
    condition     = length(var.project_id) > 0
    error_message = "The project_id value must be an non-empty string."
  }
}

variable "region" {
  type        = string
  description = "GCP Region"
  default     = "us-east4"

  validation {
    condition     = length(var.region) > 0
    error_message = "The region value must be an non-empty string."
  }
}

variable "env" {
  type        = string
  default     = "uat"
}

variable "cloudbuild_sa" {
  type        = string
  default     = "891849934010@cloudbuild.gserviceaccount.com"
  description = "Composer Service Account"
}

variable "composer_sa" {
  type        = string
  default     = "dec-cam-u-composer-sa@dec-cam-u-warehouse-9057.iam.gserviceaccount.com"
  description = "Composer Service Account"
}

variable "group_email" {
  type        = string
  default     = ""
  description = "Urbanfootprint and Aclima group name"
}

variable "github_push_tag" {
  type        = string
  default     = "-uat$"
  description = "GitHub Push Tags"
}

variable "composer_name" {
  type        = string
  default     = "dec-cam-uat"
  description = "Composer Name"
}

variable "artifact_repo" {
  type        = string
  default     = "dec-cam-api-u-ar-us-east4-ingestion-9057"
  description = "Artifact Registry Name"
}

variable "notification_channel_email-1" {
  type        = string
  default     = "abudhiraja@google.com"
  description = "Email 1"
}

variable "notification_channel_email-2" {
  type        = string
  default     = "shitole@googgle.com"
  description = "Email 2"
}

variable "notification_channel_email-3" {
  type        = string
  default     = "abinwal@google.com"
  description = "Email 3"
}

variable "read_access_sa" {
  description = "Read access on BQ"
  type  = list(string)
  default = []
}