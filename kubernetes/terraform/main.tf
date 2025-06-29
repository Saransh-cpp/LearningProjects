terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "6.41.0"
    }
  }
}

provider "google" {
  project = "cloud-academy-terraform"
  region  = "us-central1"
}

resource "google_compute_disk" "default" {
  count = 3
  name  = "test-disk-${count.index}"
  type  = "pd-ssd"
  image = "debian-cloud/debian-11"
  zone  = "us-central1-a"

  provisioner "local-exec" {
    command = "echo disk ${count.index}: ${self.self_link} >> disk_urls.txt"
  }
}