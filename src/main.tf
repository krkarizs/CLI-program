terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "3.5.0"
    }
  }
}

provider "google" {
  credentials = file(var.credentials_file)

  project = var.project
  region  = var.region
  zone    = var.zone
}

//Create Storage Bucket
resource "google_storage_bucket" "server-filez" {
  name          = "cli-server-filez"
  location      = "US"
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 3
    }
    action {
      type = "Delete"
    }
  }
}



//Upload files to the Storage Bucket (Upload database.ini, config.py, query.py, mailservice.py)
resource "google_storage_bucket_object" "server-files" {
  name       = "config.py"
  source     = "config.py"
  bucket     = "cli-server-filez"
  depends_on = [google_storage_bucket.server-filez]
}
resource "google_storage_bucket_object" "server-files2" {
  name       = "query.py"
  source     = "query.py"
  bucket     = "cli-server-filez"
  depends_on = [google_storage_bucket.server-filez]
}
resource "google_storage_bucket_object" "server-files3" {
  name       = "main.py"
  source     = "main.py"
  bucket     = "cli-server-filez"
  depends_on = [google_storage_bucket.server-filez]
}
resource "google_storage_bucket_object" "server-files4" {
  name       = "database.ini"
  source     = "database.ini"
  bucket     = "cli-server-filez"
  depends_on = [google_storage_bucket.server-filez]
}
resource "google_storage_bucket_object" "server-files5" {
  name       = "weatherconfig.ini"
  source     = "weatherconfig.ini"
  bucket     = "cli-server-filez"
  depends_on = [google_storage_bucket.server-filez]
}
resource "google_storage_bucket_object" "server-files6" {
  name       = "mailconfig.ini"
  source     = "mailconfig.ini"
  bucket     = "cli-server-filez"
  depends_on = [google_storage_bucket.server-filez]
}
resource "google_storage_bucket_object" "server-files7" {
  name       = "mailservice.py"
  source     = "mailservice.py"
  bucket     = "cli-server-filez"
  depends_on = [google_storage_bucket.server-filez]
}
resource "google_storage_bucket_object" "server-files8" {
  name       = "weather.py"
  source     = "weather.py"
  bucket     = "cli-server-filez"
  depends_on = [google_storage_bucket.server-filez]
}
resource "google_storage_bucket_object" "server-files9" {
  name       = "create_tables.py"
  source     = "create_tables.py"
  bucket     = "cli-server-filez"
  depends_on = [google_storage_bucket.server-filez]
}

resource "google_storage_bucket_object" "server-files10" {
  name       = "configcron.py"
  source     = "configcron.py"
  bucket     = "cli-server-filez"
  depends_on = [google_storage_bucket.server-filez]
}


//Create VM instance
resource "google_compute_instance" "database-server" {
  name         = "server"
  machine_type = "f1-micro"

  tags       = ["http-server", "https-server"]

  depends_on = [google_storage_bucket_object.server-files2]

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-10"
    }
  }

  network_interface {
    network = "default"

    access_config {
      // Ephemeral IP
    }
  }
  #Reads the script from a file. It is possible to write it inline as a string
  metadata_startup_script = file("startup.sh")

  service_account {
    scopes = ["cloud-platform"]
  }
}



