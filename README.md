# 🛠 MCP Server Template
## 🚀 Features
This repository is a **starter template** for building a **FastMCP server** with Python.  
It uses:

- **FastMCP** – MCP protocol server
- **Pydantic / Pydantic Settings** – type-safe configuration via environment variables
- **uv** – modern Python package manager and runtime
- **Optional Docker support** – for containerized deployment

The template helps you quickly start a production-ready MCP server with **environment-based configuration**, **optional dev tools**, and **Docker deployment**.

## ⚡Quick Start
### Local Development
```bash

# 1. Create venv
uv venv

# 2. Activate venv
## Windows
.\.venv\Scripts\activate
## macOS/Linux
source .venv/bin/activate

# 3. Install dependencies  (prod + dev)
uv sync

# 4. Run server
uv run main.py
```
----
### 🐳 Docker Deployment
#### Build image
```bash
docker build -t mcp-server .
```
#### Run **container**
```bash
docker run --env-file .env -p 8000:8000 mcp-server
```
Or with **Docker Compose**:
```bash
docker-compose up
```

## ⚙️ Configuration
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