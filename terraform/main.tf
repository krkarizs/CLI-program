terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "3.5.0"
    }
  }
}

provider "google" {
  credentials = file("C:\\Users\\KrisztinaKarizs\\Documents\\vko5-projekti\\CLI-program\\google_key.json")

  project = "terraform-demo-320306"
  region  = "us-central1"
  zone    = "us-central1-c"
}

//Create Storage Bucket
resource "google_storage_bucket" "server-files" {
  name                        = "cli-server-files"
  location                    = "US"
  force_destroy               = true

  lifecycle_rule {
    condition {
      age = 3
    }
    action {
      type = "Delete"
    }
  }
}

//Create delay
resource "time_sleep" "wait_60_seconds" {
  depends_on = [google_storage_bucket.server-files]
  create_duration = "60s"
}

resource "time_sleep" "wait_20_seconds" {
  depends_on = [google_storage_bucket_object.server-files]
  create_duration = "20s"
}

//Upload files to the Storage Bucket (Upload database.ini, config.py, query.py, mailservice.py)
resource "google_storage_bucket_object" "server-files" {
  name   = "config.py"
  source = "config.py"
  bucket = "cli-server-files"
  depends_on = [time_sleep.wait_60_seconds]
}

//Create VM instance
resource "google_compute_instance" "default" {
  name         = "server"
  machine_type = "f1-micro"

  tags = ["http-server", "https-server"]

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
  metadata_startup_script = "${file("startup.sh")}"

  service_account {
    scopes = ["storage-rw"]
  }

  depends_on = [time_sleep.wait_20_seconds]
}



