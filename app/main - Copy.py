from fastapi import FastAPI
import os
import redis
import psycopg2

app = FastAPI(title="DevOps Assignment API")


@app.get("/")
def home():
    return {
        "message": "FastAPI DevOps Assignment API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "fastapi"
    }


@app.get("/redis")
def redis_check():
    r = redis.Redis(
        host=os.getenv("REDIS_HOST", "redis"),
        port=6379,
        decode_responses=True
    )
    r.set("connection", "Redis connected successfully")
    return {
        "redis": r.get("connection")
    }


@app.get("/db")
def db_check():
    conn = psycopg2.connect(
        host=os.getenv("POSTGRES_HOST", "postgres"),
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD")
    )
    conn.close()

    return {
        "postgres": "PostgreSQL connected successfully"
    }