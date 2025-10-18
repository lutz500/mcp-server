FROM python:3.12-alpine

WORKDIR /app

# Install curl
RUN apk add --no-cache curl

# Download and install uv
RUN curl -sSL https://astral.sh/uv/install.sh | sh

# Ensure uv is in PATH
ENV PATH="/root/.local/bin:$PATH"

# Copy dependencies and install only production deps
COPY pyproject.toml uv.lock* ./
RUN uv sync --no-dev

# Copy application code
COPY src/ .

EXPOSE 8000

# Run the application
CMD ["uv", "run","--no-sync", "main.py"]
