# server.py
from core.server import mcp
from core.settings import settings

# Import tools to register them with the MCP instance
import tools.postgres  # noqa F401
import tools.math  # noqa F401


def main():
    mcp.run(
        transport=settings.TRANSPORT,
        host=settings.SERVER_HOST,
        port=settings.SERVER_PORT,
        show_banner=False,
    )


if __name__ == "__main__":
    main()
