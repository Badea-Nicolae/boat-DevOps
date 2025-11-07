# Boat DevOps Project

A DevOps application for boat monitoring, including engine telemetry and waypoint management. Built with FastAPI and includes full CI/CD pipeline, Docker containerization, Ansible deployment, Terraform infrastructure, and Prometheus monitoring.

## Features

- Engine monitoring (RPM, temperature, oil pressure)
- Waypoint management (create, list, delete)
- RESTful API with OpenAPI/Swagger documentation
- Docker containerization
- Infrastructure as Code with Terraform
- Automated deployment with Ansible
- Monitoring with Prometheus

## Local Development Setup

1. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

4. Access the API:
- API endpoints: http://localhost:8000/api/v1/
- Swagger documentation: http://localhost:8000/docs
- ReDoc documentation: http://localhost:8000/redoc

## Testing

Run tests using pytest:
```bash
pytest app/tests/
```

## Docker Setup

1. Build the image:
```bash
docker build -t boat-app .
```

2. Run with Docker Compose:
```bash
docker-compose up
```

The application will be available at http://localhost:8000

## Deployment

### Infrastructure Setup (Terraform)

1. Configure your DigitalOcean credentials:
```bash
export DO_TOKEN="your-token"
```

2. Initialize and apply Terraform:
```bash
cd infra/terraform
terraform init
terraform apply
```

### Application Deployment (Ansible)

1. Update inventory file with your server details:
```bash
cd deploy/ansible
vim inventory.ini
```

2. Run the Ansible playbook:
```bash
ansible-playbook -i inventory.ini site.yml
```

## Monitoring

Prometheus monitoring is configured in `monitoring/prometheus.yml`. After deployment, metrics are available at:
- Application metrics: http://your-server:8000/metrics
- Prometheus: http://your-server:9090

## API Documentation

### Engine Endpoints

- GET `/api/v1/engine` - Get current engine state
- POST `/api/v1/engine` - Update engine metrics

### Waypoint Endpoints

- GET `/api/v1/waypoints` - List all waypoints
- POST `/api/v1/waypoints` - Create new waypoint
- DELETE `/api/v1/waypoints/{id}` - Delete a waypoint

For detailed API documentation, refer to the Swagger UI at `/docs` when the application is running.
