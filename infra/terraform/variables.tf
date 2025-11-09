variable "do_token" {
  type        = string
  description = "DigitalOcean API token"
  sensitive   = true
}

variable "region" {
  type        = string
  description = "DigitalOcean region for deployment"
  default     = "fra1"
  validation {
    condition     = can(regex("^[a-z]{3}\\d$", var.region))
    error_message = "Region must be a valid DigitalOcean region code (e.g., fra1, nyc1, etc.)"
  }
}

variable "size" {
  type        = string
  description = "DigitalOcean droplet size"
  default     = "s-1vcpu-1gb"
  validation {
    condition     = can(regex("^s-\\d+vcpu-\\d+gb$", var.size))
    error_message = "Size must be a valid DigitalOcean droplet size (e.g., s-1vcpu-1gb)"
  }
}

variable "ssh_fingerprint" {
  type        = string
  description = "SSH key fingerprint for server access"
  validation {
    condition     = length(var.ssh_fingerprint) > 0
    error_message = "SSH fingerprint cannot be empty"
  }
}
