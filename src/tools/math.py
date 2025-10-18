from utils.logger import logger
from core.server import mcp


@mcp.tool
def add(x: int, y: int) -> int:
    """Add two numbers."""
    logger.info(f"Adding {x} and {y}")
    return x + y


@mcp.tool
def subtract(x: int, y: int) -> int:
    """Subtract two numbers."""
    logger.info(f"Subtracting {y} from {x}")
    return x - y
