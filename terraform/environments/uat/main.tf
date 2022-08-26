# project-specific locals
locals {
  env              = var.env
  region           = var.region
  project_id       = var.project_id
}

module "bigquery" {
	source                = "../../modules/bigquery"
    project_id            = local.project_id
    composer_sa           = var.composer_sa
    group_email           = var.group_email
    cloudbuild_sa         = var.cloudbuild_sa
    read_access_sa        = var.read_access_sa
}

module "monitoring" {
  source                       = "../../modules/monitoring"
  project_id                   = local.project_id
  env                          = var.env
  composer_name                = var.composer_name
  composer_location            = local.region
  notification_channel_email-1 = var.notification_channel_email-1
  notification_channel_email-2 = var.notification_channel_email-2
  notification_channel_email-3 = var.notification_channel_email-3
}

