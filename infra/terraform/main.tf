terraform {
  required_providers {
    digitalocean = {
      source = "digitalocean/digitalocean"
      version = "~> 2.40"
    }
  }
}

provider "digitalocean" {
  token = var.do_token
}

resource "digitalocean_droplet" "app" {
  image  = "ubuntu-22-04-x64"
  name   = "boatapp-prod"
  region = var.region
  size   = var.size
  ssh_keys = [var.ssh_fingerprint]
}

output "droplet_ip" {
  value = digitalocean_droplet.app.ipv4_address
}
