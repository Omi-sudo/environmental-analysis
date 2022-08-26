## Logging metrics
resource "google_logging_metric" "logging_metric" {
  name   = "composer-log/metric"
  filter = "resource.type=\"cloud_composer_environment\" AND resource.labels.environment_name=\"${var.composer_name}\" AND resource.labels.location=\"${var.composer_location}\" AND logName=\"projects/${var.project_id}/logs/airflow-worker\" AND severity=ERROR"
  metric_descriptor {
    metric_kind = "DELTA"
    value_type  = "INT64"
  }
  description = "Log Metrics for Cloud Composer TF"
}

## Notification Channel ##
resource "google_monitoring_notification_channel" "email_notification_channel-1" {
  display_name = "Email-1"
  enabled      = "true"

  labels = {
    email_address = var.notification_channel_email-1
  }

  project = var.project_id
  type    = "email"
}

resource "google_monitoring_notification_channel" "email_notification_channel-2" {
  display_name = "Email-2"
  enabled      = "true"

  labels = {
    email_address = var.notification_channel_email-2
  }

  project = var.project_id
  type    = "email"
}

resource "google_monitoring_notification_channel" "email_notification_channel-3" {
  display_name = "Email-3"
  enabled      = "true"

  labels = {
    email_address = var.notification_channel_email-3
  }

  project = var.project_id
  type    = "email"
}

resource "google_monitoring_alert_policy" "composer-task-failed-tf" {
  combiner = "OR"
  depends_on = [
    google_logging_metric.logging_metric,
    google_monitoring_notification_channel.email_notification_channel-1,
    google_monitoring_notification_channel.email_notification_channel-2,
    google_monitoring_notification_channel.email_notification_channel-3
  ]
  conditions {
    condition_threshold {
      aggregations {
        alignment_period     = "60s"
        cross_series_reducer = "REDUCE_COUNT"
        per_series_aligner   = "ALIGN_COUNT"
      }

      comparison      = "COMPARISON_GT"
      duration        = "0s"
      filter          = "metric.type=\"logging.googleapis.com/user/composer-log/metric\" resource.type=\"cloud_composer_environment\""
      threshold_value = "0"

      trigger {
        count   = "1"
        percent = "0"
      }
    }

    display_name = "${var.env} - Composer Alert TF"
  }

  documentation {
    content = "Hi Team, Errors occurred in ${var.env} Cloud Composer Workflow.  "
  }

  display_name          = "${var.env} - Composer Alert Policy TF"
  enabled               = "true"
  notification_channels = [google_monitoring_notification_channel.email_notification_channel-1.name, google_monitoring_notification_channel.email_notification_channel-2.name, google_monitoring_notification_channel.email_notification_channel-3.name]
  project               = var.project_id
}