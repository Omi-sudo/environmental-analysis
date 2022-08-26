locals {

}

### Reporting Dataset Start ####

resource "google_bigquery_dataset" "reporting" {
  project                     = var.project_id
  dataset_id                  = var.reporting
  description                 = "Dataset that can be used to create reports. Contains all transformed values."
  location                    = var.dataset_location
}

resource "google_bigquery_dataset_iam_binding" "bindings_reporting" {
  project    = var.project_id
  dataset_id = google_bigquery_dataset.reporting.dataset_id
  role       = "roles/bigquery.admin"
  members    = [
    format("serviceAccount:%s", var.composer_sa)
  ]
}

resource "google_bigquery_dataset_iam_binding" "binding_reporting_reader" {
  project    = var.project_id
  dataset_id = google_bigquery_dataset.reporting.dataset_id
  role       = "roles/bigquery.dataViewer"
  members    = var.read_access_sa
}

resource "google_bigquery_table" "reporting" {
  for_each        = var.reporting_tables
  project         = var.project_id
  dataset_id      = google_bigquery_dataset.reporting.dataset_id
  table_id        = each.key
  friendly_name   = each.value.friendly_name
  description     = each.value.description
  clustering      = try(each.value.options.clustering, null)
  expiration_time = try(each.value.options.expiration_time, null)
  schema          = file(each.value.schema)
  deletion_protection = false  # Remove after successful apply

  dynamic "time_partitioning" {
    for_each = try(each.value.partitioning.time, null) != null ? [""] : []
    content {
      expiration_ms = each.value.partitioning.time.expiration_ms
      field         = each.value.partitioning.field
      type          = each.value.partitioning.time.type
    }
  }
}

### Reporting Dataset End ####


### Reporting View Dataset Start ####

resource "google_bigquery_dataset" "reporting_views" {
  project                     = var.project_id
  dataset_id                  = var.reporting_views
  description                 = "Dataset contains the views to transform the values to Geography."
  location                    = var.dataset_location
}

resource "google_bigquery_dataset_iam_binding" "bindings_reporting_views" {
  project    = var.project_id
  dataset_id = google_bigquery_dataset.reporting_views.dataset_id
  role       = "roles/bigquery.admin"
  members    = [
    format("serviceAccount:%s", var.composer_sa)
  ]
}

resource "google_bigquery_table" "views" {
  depends_on    = [google_bigquery_table.ingestion, google_bigquery_table.ingestion_aqs,
                    google_bigquery_table.ingestion_arcgis, google_bigquery_table.ingestion_socrata,
                    google_bigquery_table.warehouse]
  for_each      = var.reporting_vw
  project       = var.project_id
  dataset_id    = google_bigquery_dataset.reporting_views.dataset_id
  table_id      = each.key
  friendly_name = each.value.friendly_name
  description   = "Terraform managed."
  deletion_protection=false

  view {
    query          = file(each.value.query)
    use_legacy_sql = each.value.use_legacy_sql
  }
}

resource "google_bigquery_routine" "procedures" {
  for_each = var.reporting_procedures
  project = var.project_id
  dataset_id = google_bigquery_dataset.reporting_views.dataset_id
  routine_id = each.value.routine_id
  language = "SQL"
  routine_type = "PROCEDURE"
  depends_on = [
    google_bigquery_dataset.warehouse
  ]
  definition_body = file(each.value.definition_body)
  arguments {
    name = "ingestion_time_ts"
    data_type = "{\"typeKind\" :  \"TIMESTAMP\"}"
  }
}

### Reporting View Dataset End ####


### Warehouse Dataset Start ####
resource "google_bigquery_dataset" "warehouse" {
  project                     = var.project_id
  dataset_id                  = var.warehouse
  description                 = "Dataset that contains the snapshot of the data on which the job has started."
  location                    = var.dataset_location
}

resource "google_bigquery_dataset_iam_binding" "bindings_warehouse" {
  project    = var.project_id
  dataset_id = google_bigquery_dataset.warehouse.dataset_id
  role       = "roles/bigquery.admin"
  members    = [
    format("serviceAccount:%s", var.composer_sa)
  ]
}

resource "google_bigquery_table" "warehouse" {
  for_each        = var.warehouse_tables
  project         = var.project_id
  dataset_id      = google_bigquery_dataset.warehouse.dataset_id
  table_id        = each.key
  friendly_name   = each.value.friendly_name
  description     = each.value.description
  clustering      = try(each.value.options.clustering, null)
  expiration_time = try(each.value.options.expiration_time, null)
  schema          = file(each.value.schema)
  deletion_protection = false  # Remove after successful apply

  dynamic "time_partitioning" {
    for_each = try(each.value.partitioning.time, null) != null ? [""] : []
    content {
      expiration_ms = each.value.partitioning.time.expiration_ms
      field         = each.value.partitioning.field
      type          = each.value.partitioning.time.type
    }
  }
}
### Warehouse Dataset End ####


### Ingestion Dataset Start ####
resource "google_bigquery_dataset" "ingestion" {
  project                     = var.project_id
  dataset_id                  = var.ingestion
  description                 = "Dataset that contains the raw data of the flat files."
  location                    = var.dataset_location
}

resource "google_bigquery_dataset_iam_binding" "bindings_ingestion" {
  project    = var.project_id
  dataset_id = google_bigquery_dataset.ingestion.dataset_id
  role       = "roles/bigquery.admin"
  members    = [
    format("serviceAccount:%s", var.composer_sa)
  ]
}

resource "google_bigquery_table" "ingestion" {
  for_each        = var.ingestion_tables
  project         = var.project_id
  dataset_id      = google_bigquery_dataset.ingestion.dataset_id
  table_id        = each.key
  friendly_name   = each.value.friendly_name
  description     = each.value.description
  clustering      = try(each.value.options.clustering, null)
  expiration_time = try(each.value.options.expiration_time, null)
  schema          = file(each.value.schema)
  deletion_protection = false  # Remove after successful apply

  dynamic "time_partitioning" {
    for_each = try(each.value.partitioning.time, null) != null ? [""] : []
    content {
      expiration_ms = each.value.partitioning.time.expiration_ms
      field         = each.value.partitioning.field
      type          = each.value.partitioning.time.type
    }
  }
}
### Ingestion Dataset End ####


### Ingestion ArcGIS Dataset Start ####
resource "google_bigquery_dataset" "ingestion_arcgis" {
  project                     = var.project_id
  dataset_id                  = var.ingestion_arcgis
  description                 = "Dataset that contains the ArcGIS raw data of the flat files."
  location                    = var.dataset_location
}

resource "google_bigquery_dataset_iam_binding" "bindings_ingestion_arcgis" {
  project    = var.project_id
  dataset_id = google_bigquery_dataset.ingestion_arcgis.dataset_id
  role       = "roles/bigquery.admin"
  members    = [
    format("serviceAccount:%s", var.composer_sa)
  ]
}

resource "google_bigquery_table" "ingestion_arcgis" {
  for_each        = var.ingestion_arcgis_tables
  project         = var.project_id
  dataset_id      = google_bigquery_dataset.ingestion_arcgis.dataset_id
  table_id        = each.key
  friendly_name   = each.value.friendly_name
  description     = each.value.description
  clustering      = try(each.value.options.clustering, null)
  expiration_time = try(each.value.options.expiration_time, null)
  schema          = file(each.value.schema)
  deletion_protection = false  # Remove after successful apply

  dynamic "time_partitioning" {
    for_each = try(each.value.partitioning.time, null) != null ? [""] : []
    content {
      expiration_ms = each.value.partitioning.time.expiration_ms
      field         = each.value.partitioning.field
      type          = each.value.partitioning.time.type
    }
  }
}
### Ingestion ArcGIS Dataset End ####


### Ingestion Socrata Dataset Start ####
resource "google_bigquery_dataset" "ingestion_socrata" {
  project                     = var.project_id
  dataset_id                  = var.ingestion_socrata
  description                 = "Dataset that contains the Socrata raw data of the flat files."
  location                    = var.dataset_location
}

resource "google_bigquery_dataset_iam_binding" "bindings_ingestion_socrata" {
  project    = var.project_id
  dataset_id = google_bigquery_dataset.ingestion_socrata.dataset_id
  role       = "roles/bigquery.admin"
  members    = [
    format("serviceAccount:%s", var.composer_sa)
  ]
}

resource "google_bigquery_table" "ingestion_socrata" {
  for_each        = var.ingestion_socrata_tables
  project         = var.project_id
  dataset_id      = google_bigquery_dataset.ingestion_socrata.dataset_id
  table_id        = each.key
  friendly_name   = each.value.friendly_name
  description     = each.value.description
  clustering      = try(each.value.options.clustering, null)
  expiration_time = try(each.value.options.expiration_time, null)
  schema          = file(each.value.schema)
  deletion_protection = false  # Remove after successful apply

  dynamic "time_partitioning" {
    for_each = try(each.value.partitioning.time, null) != null ? [""] : []
    content {
      expiration_ms = each.value.partitioning.time.expiration_ms
      field         = each.value.partitioning.field
      type          = each.value.partitioning.time.type
    }
  }
}
### Ingestion Socrata Dataset End ####


### Ingestion AQS Dataset Start ####
resource "google_bigquery_dataset" "ingestion_aqs" {
  project                     = var.project_id
  dataset_id                  = var.ingestion_aqs
  description                 = "Dataset that contains the AQS raw data of the flat files."
  location                    = var.dataset_location
}

resource "google_bigquery_dataset_iam_binding" "bindings_ingestion_aqs" {
  project    = var.project_id
  dataset_id = google_bigquery_dataset.ingestion_aqs.dataset_id
  role       = "roles/bigquery.admin"
  members    = [
    format("serviceAccount:%s", var.composer_sa)
  ]
}

resource "google_bigquery_table" "ingestion_aqs" {
  for_each        = var.ingestion_aqs_tables
  project         = var.project_id
  dataset_id      = google_bigquery_dataset.ingestion_aqs.dataset_id
  table_id        = each.key
  friendly_name   = each.value.friendly_name
  description     = each.value.description
  clustering      = try(each.value.options.clustering, null)
  expiration_time = try(each.value.options.expiration_time, null)
  schema          = file(each.value.schema)
  deletion_protection = false  # Remove after successful apply

  dynamic "time_partitioning" {
    for_each = try(each.value.partitioning.time, null) != null ? [""] : []
    content {
      expiration_ms = each.value.partitioning.time.expiration_ms
      field         = each.value.partitioning.field
      type          = each.value.partitioning.time.type
    }
  }
}
### Ingestion AQS Dataset End ####


### Ingestion FTP Dataset Start ####
resource "google_bigquery_dataset" "ingestion_ftp" {
  project                     = var.project_id
  dataset_id                  = var.ingestion_ftp
  description                 = "Dataset that contains the AQS raw data of the flat files."
  location                    = var.dataset_location
}

resource "google_bigquery_dataset_iam_binding" "bindings_ingestion_ftp" {
  project    = var.project_id
  dataset_id = google_bigquery_dataset.ingestion_ftp.dataset_id
  role       = "roles/bigquery.admin"
  members    = [
    format("serviceAccount:%s", var.composer_sa)
  ]
}

resource "google_bigquery_table" "ingestion_ftp" {
  for_each        = var.ingestion_ftp_tables
  project         = var.project_id
  dataset_id      = google_bigquery_dataset.ingestion_ftp.dataset_id
  table_id        = each.key
  friendly_name   = each.value.friendly_name
  description     = each.value.description
  clustering      = try(each.value.options.clustering, null)
  expiration_time = try(each.value.options.expiration_time, null)
  schema          = file(each.value.schema)
  deletion_protection = false  # Remove after successful apply

  dynamic "time_partitioning" {
    for_each = try(each.value.partitioning.time, null) != null ? [""] : []
    content {
      expiration_ms = each.value.partitioning.time.expiration_ms
      field         = each.value.partitioning.field
      type          = each.value.partitioning.time.type
    }
  }
}
### Ingestion FTP Dataset End ####

### Job Metadata Dataset Start ####
resource "google_bigquery_dataset" "job_metadata" {
  project                     = var.project_id
  dataset_id                  = var.job_metadata
  description                 = "Dataset that contains the AQS raw data of the flat files."
  location                    = var.dataset_location
}

resource "google_bigquery_dataset_iam_binding" "bindings_job_metadata" {
  project    = var.project_id
  dataset_id = google_bigquery_dataset.job_metadata.dataset_id
  role       = "roles/bigquery.admin"
  members    = [
    format("serviceAccount:%s", var.composer_sa)
  ]
}

resource "google_bigquery_table" "job_metadata" {
  for_each        = var.job_metadata_tables
  project         = var.project_id
  dataset_id      = google_bigquery_dataset.job_metadata.dataset_id
  table_id        = each.key
  friendly_name   = each.value.friendly_name
  description     = each.value.description
  clustering      = try(each.value.options.clustering, null)
  expiration_time = try(each.value.options.expiration_time, null)
  schema          = file(each.value.schema)
  deletion_protection = false  # Remove after successful apply

  dynamic "time_partitioning" {
    for_each = try(each.value.partitioning.time, null) != null ? [""] : []
    content {
      expiration_ms = each.value.partitioning.time.expiration_ms
      field         = each.value.partitioning.field
      type          = each.value.partitioning.time.type
    }
  }
}
### Job Metadata Dataset End ####