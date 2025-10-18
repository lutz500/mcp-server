from fastmcp import FastMCP
from core.settings import settings

# Initialize the MCP server instance
mcp = FastMCP(name=settings.SERVER_NAME)
