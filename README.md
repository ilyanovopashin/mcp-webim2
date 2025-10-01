# WorldTime MCP Server

This repository contains a simple Model Context Protocol (MCP) server that exposes a
single tool for retrieving timezone data from [WorldTimeAPI](http://worldtimeapi.org).

## Features

- **`get_timezones` tool** – Fetch the list of timezones for a given region
  (defaults to `Europe`).

## Installation

```bash
pip install .
```

## Usage

Run the server directly:

```bash
python -m worldtime_server
```

Or use the console script entry point:

```bash
worldtime-mcp-server
```

Once running, connect your MCP-compatible client (such as the n8n AI agent) to the
server. Call the `get_timezones` tool and optionally supply a different region, for
example `America` or `Asia/Tokyo`.


## Deploying on Vercel

This repository is pre-configured for deployment on [Vercel](https://vercel.com/):

1. Install dependencies locally and test the server:

   ```bash
   pip install -r requirements.txt
   python -m compileall worldtime_server.py
   ```

2. Log in to Vercel and deploy:

   ```bash
   vercel deploy --prod
   ```

   The deployment exposes two routes:

   - `GET /` – A simple health endpoint that returns `{ "status": "ok" }`.
   - `POST /mcp` – The Streamable HTTP transport endpoint for MCP clients.

3. Configure your MCP-compatible client to use the deployed `/mcp` endpoint.

