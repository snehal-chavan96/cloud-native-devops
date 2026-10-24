# Cloud-Native Application Using Docker and Kubernetes

## 1. Project Overview

This project demonstrates the containerization and deployment of a Python Flask web application using Docker and Kubernetes. The application displays a welcome page and provides a health-check endpoint.

## 2. Technologies Used

- Python
- Flask
- Docker
- Kubernetes
- Minikube
- kubectl
- Git and GitHub

## 3. Project Structure

- `app.py` — Python Flask application
- `requirements.txt` — Python dependencies
- `Dockerfile` — Instructions to build the Docker image
- `deployment.yaml` — Kubernetes Deployment configuration
- `service.yaml` — Kubernetes Service configuration
- `README.md` — Project documentation

## 4. Build and Run Using Docker

Build the image:

```bash
docker build -t cloud-native-app:v1 .
```

Run the container:

```bash
docker run -d --name cloud-native-container -p 5000:5000 cloud-native-app:v1
```

Access the application at `http://localhost:5000`.

## 5. Deploy Using Kubernetes

Start Minikube:

```bash
minikube start --driver=docker
```

Build the image inside Minikube:

```bash
minikube image build -t cloud-native-app:v1 .
```

Deploy the application:

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

Verify the resources:

```bash
kubectl get deployments,pods,services
```

Access the Service:

```bash
minikube service cloud-native-service --url
```

## 6. Application Endpoints

- `/` — Displays the welcome page.
- `/health` — Returns the application health status.

## 7. Kubernetes Configuration

The Deployment specifies two replicas to demonstrate replicated application workloads. The NodePort Service exposes the application through port `30080` on the Kubernetes node.

## 8. Learning Outcomes

This project demonstrates Docker image creation, container execution, Kubernetes Deployment configuration, Service-based networking, health checks, and application verification.

## 9. Repository

GitHub repository: Add your repository URL here.

## 10. Evidence

Add your screenshots or demonstration video link here after completing and testing the project.