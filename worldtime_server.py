"""WorldTimeAPI MCP server."""
from __future__ import annotations

import json
from typing import Any

import httpx


# Configure the MCP server for both local execution (stdio transport) and
# deployment on serverless platforms such as Vercel. The ``stateless_http`` flag
# ensures that HTTP sessions do not rely on in-memory state that would be lost
# between invocations of a serverless function.
server = FastMCP(
    "worldtime",
    stateless_http=True,
)



async def get_timezones(region: str = "Europe") -> str:
    """Return the list of timezones for a WorldTimeAPI region.

    Args:
        region: The region segment in the WorldTimeAPI timezone endpoint.
            Defaults to ``"Europe"``.

    Returns:
        A pretty-printed JSON string containing the API response.

    Raises:
        ValueError: If the request fails or the region is invalid.
    """

    region = region.strip()
    if not region:
        raise ValueError("Region must be a non-empty string.")

    url = f"http://worldtimeapi.org/api/timezone/{region}"

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, timeout=10.0)
            response.raise_for_status()
    except httpx.HTTPStatusError as exc:  # pragma: no cover - descriptive message
        raise ValueError(
            f"WorldTimeAPI returned status {exc.response.status_code}: {exc.response.text}"
        ) from exc
    except httpx.HTTPError as exc:  # pragma: no cover - descriptive message
        raise ValueError(f"Failed to reach WorldTimeAPI: {exc}") from exc

    data: Any = response.json()
    return json.dumps(data, indent=2, ensure_ascii=False)


def main() -> None:
    """Run the WorldTimeAPI MCP server."""

    server.run()


if __name__ == "__main__":
    main()
