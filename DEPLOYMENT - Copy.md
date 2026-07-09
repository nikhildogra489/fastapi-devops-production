# Deployment Guide

## Server

- AWS EC2 Ubuntu 24.04 LTS
- Docker
- Docker Compose
- NGINX
- PostgreSQL
- Redis

---

## Clone Repository

```bash
git clone https://github.com/nikhildogra489/fastapi-devops-production.git
cd fastapi-devops-production
```

---

## Create Environment File

```bash
nano .env
```

Example:

```
POSTGRES_DB=devopsdb
POSTGRES_USER=devops
POSTGRES_PASSWORD=devops123
POSTGRES_HOST=postgres

REDIS_HOST=redis
```

---

## Build Application

```bash
docker compose up -d --build
```

---

## Verify Containers

```bash
docker compose ps
```

---

## Test Endpoints

```bash
curl http://localhost/
curl http://localhost/health
curl http://localhost/db
curl http://localhost/redis
```

---

## GitHub Actions Deployment

Every push to the **main** branch automatically:

1. Connects to EC2 using SSH
2. Pulls the latest code
3. Rebuilds Docker containers
4. Restarts the application

---

## Restart Application

```bash
docker compose restart
```

---

## View Logs

```bash
docker compose logs
```

or

```bash
docker compose logs fastapi
```

---

## Stop Application

```bash
docker compose down
```

---

## Security

- SSH key authentication
- AWS Security Groups
- Environment variables
- Docker container isolation

---

## SSL

For production:

- Use Let's Encrypt + Certbot
- Configure NGINX for HTTPS
- Or use Cloudflare as a reverse proxy

---

## Backup Strategy

PostgreSQL data is stored in Docker volumes.

Example backup:

```bash
docker exec postgres_db pg_dump -U devops devopsdb > backup.sql
```

---

## Health Check

```text
GET /health
```

Returns:

```json
{
  "status":"healthy",
  "service":"fastapi"
}
```