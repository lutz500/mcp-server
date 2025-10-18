from utils.api_handler import APIClient
from core.settings import settings
from core.server import mcp

# Base URL for the internal API
internal_api_client = APIClient(base_url=settings.INTERNAL_API_URL)


@mcp.tool
def get_databases() -> list[str]:
    """
    Fetch the list of all available databases from the internal API.

    Returns:
        list[str]: A list of database names currently available on the server.

    Raises:
        ConnectionError: If the internal API is unreachable.
        httpx.HTTPStatusError: If the API returns a non-2xx status code.

    Example:
        >>> get_databases()
        ["sales_db", "inventory_db", "analytics_db"]

    Notes:
        - This tool does not require any input parameters.
        - The agent can use this list to select the target database for other operations.
    """
    return internal_api_client.get("/database") or []


@mcp.tool
def get_products(database: str) -> list[dict]:
    """
    Fetch the list of products from a specific database in the internal API.

    Args:
        database (str): The name of the target database to query products from.

    Returns:
        list[dict]: A list of product objects, each typically containing
                    keys like 'id', 'name', 'price', and 'stock'.

    Raises:
        ConnectionError: If the internal API is unreachable.
        httpx.HTTPStatusError: If the API returns a non-2xx status code.

    Example:
        >>> get_products("inventory_db")
        [
            {"id": 101, "name": "Laptop", "price": 1200, "stock": 15},
            {"id": 102, "name": "Mouse", "price": 25, "stock": 200}
        ]

    Notes:
        - The 'database' header is required by the API to select the target database.
        - The agent should ensure the database exists (use get_databases() first) before calling this function.
    """
    headers = {"databaseName": database}
    return internal_api_client.get("/products", headers=headers) or []
