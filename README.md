# MCP Server Template

## Overview
This repository is a **starter template** for building a **FastMCP server** with Python.  
It uses:

- **FastMCP** – MCP protocol server
- **Pydantic / Pydantic Settings** – type-safe configuration via environment variables
- **uv** – modern Python package manager and runtime
- **Optional Docker support** – for containerized deployment

The template helps you quickly start a production-ready MCP server with **environment-based configuration**, **optional dev tools**, and **Docker deployment**.

## Installation

### Local Development

#### 1. Create and activate venv

```bash
uv venv
# Windows
.\.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```
#### 2. Install dependencies
```bash
uv sync        # installs both prod + dev dependencies
```

#### 3. Run server
```bash
uv run main.py
```

### Docker Deployment
#### 1. Build image
```bash
docker build -t mcp-server .
```
#### 2. Run container
With docker run:
```bash
docker run --env-file .env -p 8000:8000 mcp-server
```
Or with Docker Compose:

```bash
docker-compose up
```

## Configuration
The server get configured using environment variables.  
Create a `.env` file in the root directory or set them in the `docker-compose.yaml`

```yaml
# ---- [Optional]: Server Settings ----
# Those values are also set as default values!
SERVER_NAME=MCP-Server
SERVER_HOST=0.0.0.0
SERVER_PORT=8000
TRANSPORT=http

# ---- [Optional]: ENV-Vars ----
API_URL=https://test-api.com/v1/users
```
Behavior:
- Environment variables take highest precedence
- .env file is used as fallback
- Class defaults are used if neither is set

There are logs shown if certain variables are not set!