"""Vercel entry point for the WorldTime MCP server."""

from starlette.requests import Request
from starlette.responses import JSONResponse

from worldtime_server import server

# Instantiate the ASGI application exposed by FastMCP for streamable HTTP
# transports. The object is created once at import time so that Vercel can reuse
# it between invocations when possible.
app = server.streamable_http_app()


@app.route("/")
@app.route("/api/index")
async def root(_: Request) -> JSONResponse:
    """Provide a simple health endpoint for Vercel deployments."""

    return JSONResponse({"status": "ok"})
