# FastAPI DevOps Production Deployment

## Project Overview

This project demonstrates a production-ready deployment of a FastAPI application using Docker, Docker Compose, PostgreSQL, Redis, NGINX Reverse Proxy, and GitHub Actions on an AWS EC2 instance.

The project showcases a complete DevOps workflow including containerization, reverse proxy configuration, automated deployment, health monitoring, logging strategy, backup strategy, and infrastructure documentation.

---

## Tech Stack

- FastAPI
- Docker
- Docker Compose
- PostgreSQL 16
- Redis 7
- NGINX
- AWS EC2 (Ubuntu)
- GitHub Actions
- Git

---

## Architecture

```
                GitHub
                   │
          GitHub Actions (CI/CD)
                   │
              SSH Deployment
                   │
              AWS EC2 Server
                   │
               NGINX Proxy
                   │
               FastAPI App
              /           \
      PostgreSQL        Redis
```

---

## Project Structure

```
.
├── app/
│   ├── Dockerfile
│   ├── main.py
│   └── requirements.txt
│
├── nginx/
│   └── default.conf
│
├── .github/
│   └── workflows/
│       └── deploy.yml
│
├── docker-compose.yml
├── .env.example
├── DEPLOYMENT.md
└── README.md
```

---

## Features

- Dockerized FastAPI application
- Docker Compose orchestration
- PostgreSQL database
- Redis cache
- NGINX Reverse Proxy
- Environment variable configuration
- Health Check endpoint
- GitHub Actions CI/CD
- AWS EC2 deployment
- Production-ready project structure

---

## Health Check

```
GET /health
```

Response

```json
{
  "status": "healthy",
  "service": "fastapi"
}
```

---

## Environment Variables

Create a `.env` file.

Example:

```
POSTGRES_DB=fastapi_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=postgres

REDIS_HOST=redis
```

---

## Run Locally

Clone repository

```
git clone https://github.com/your-username/fastapi-devops-production.git
```

Go inside project

```
cd fastapi-devops-production
```

Build

```
docker compose up -d --build
```

---

## Deployment

The application is deployed on an AWS EC2 Ubuntu instance using Docker Compose.

NGINX acts as the reverse proxy.

GitHub Actions automatically deploys the application whenever code is pushed to the main branch.

---

## Logging Strategy

- Docker container logs
- FastAPI application logs
- NGINX access logs
- NGINX error logs

Logs can be viewed using:

```
docker compose logs
```

---

## Backup Strategy

- PostgreSQL data stored in Docker Volume
- Redis data stored in Docker Volume
- Volumes can be backed up regularly
- Docker restart policy ensures automatic recovery

---

## Security Measures

- Ubuntu server
- SSH key authentication
- AWS Security Groups
- Docker container isolation
- Environment variables for secrets

---

## SSL Approach

Since no custom domain is available, SSL is documented for production deployment.

Recommended approach:

- Let's Encrypt
- Certbot
- Cloudflare Proxy

---

## CI/CD

GitHub Actions automatically:

- Connects to EC2
- Pulls latest code
- Rebuilds Docker containers
- Restarts the application

---

## API Endpoints

| Endpoint | Description |
|----------|-------------|
| / | Home |
| /health | Health Check |
| /db | PostgreSQL Test |
| /redis | Redis Test |

---

## Author

**Nikhil Dogra**