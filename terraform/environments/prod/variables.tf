variable "project_id" {
  type        = string
  description = "GCP Project ID"
  default     = "dec-cam-p-warehouse-d356"

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
  default     = "prod"
}

variable "cloudbuild_sa" {
  type        = string
  default     = "891849934010@cloudbuild.gserviceaccount.com"
  description = "Composer Service Account"
}

variable "composer_sa" {
  type        = string
  default     = "dec-cam-p-composer-sa@dec-cam-p-warehouse-d356.iam.gserviceaccount.com"
  description = "Composer Service Account"
}

variable "group_email" {
  type        = string
  default     = ""
  description = "Urbanfootprint and Aclima group name"
}

variable "github_push_tag" {
  type        = string
  default     = "-prod$"
  description = "GitHub Push Tags"
}

variable "composer_name" {
  type        = string
  default     = "dec-cam-prod"
  description = "Composer Name"
}

variable "artifact_repo" {
  type        = string
  default     = "dec-cam-api-p-ar-us-east4-ingestion-d356"
  description = "Artifact Registry Name"
}

variable "notification_channel_email-1" {
  type        = string
  default     = "Amanda.Teora@dec.ny.gov"
  description = "Email 1"
}

variable "notification_channel_email-2" {
  type        = string
  default     = "kevin.mcgarry@dec.ny.gov"
  description = "Email 2"
}

variable "notification_channel_email-3" {
  type        = string
  default     = "George.Kipp@its.ny.gov"
  description = "Email 3"
}

variable "read_access_sa" {
  description = "Read access on BQ"
  type        = list(string)
  default     = ["serviceAccount:datapipes-operators-gke@aclima-test.iam.gserviceaccount.com",
                "serviceAccount:datapipes-operators-gke@aclima-lab.iam.gserviceaccount.com",
                "serviceAccount:uf-data-pipeline@data-science-team-276319.iam.gserviceaccount.com",
                "group:google-dec-cam-aclima-staff-public@its.ny.gov",
                "group:google-dec-cam-aclima-staff-all@its.ny.gov"]
}
