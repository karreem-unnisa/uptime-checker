# 🕵️‍♂️ Uptime Checker API

This is a simple Flask-based API that checks if a given URL is online.

## 🔧 Endpoints

- `GET /` - Welcome route
- `GET /check?url=<your-url>` - Checks if the site is up

## 🚀 Run Locally

```bash
docker build -t uptime-checker .
docker run -p 5000:5000 uptime-checker
