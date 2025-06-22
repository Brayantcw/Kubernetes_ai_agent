# Kubernetes AI Agent

This repository provides a minimal example of creating an AI agent that interacts with a Kubernetes cluster via the Google ADK MCP server.

## Overview

The code uses the Google ADK agent framework to discover Kubernetes tools from an MCP server and then builds an `Agent` configured with those tools. The agent's behaviour is guided by prompts defined in `prompts.py`.

## Repository layout

- `Kubernetes_agent/agent.py` – asynchronous helper functions for discovering MCP tools and constructing the agent.
- `Kubernetes_agent/prompts.py` – text prompts and instructions returned to the agent.
- `Kubernetes_agent/__init__.py` – exposes the `root_agent` coroutine for import.
- `.env` – example environment variables used by the Google ADK backend.

## Getting started

1. Install the required Python dependencies for Google ADK and any MCP tooling. For example:
   ```bash
   pip install -r requirements.txt
   ```
2. Copy `.env` and adjust the values for your environment (API keys, backend selection, etc.).
3. Create the agent in your own code:
   ```python
   from Kubernetes_agent import root_agent
   import asyncio

   agent, cleanup = asyncio.run(root_agent)
   ```
   The returned `agent` is ready to handle Kubernetes-related tasks using the MCP tools.

This project is intended as a simple demonstration of how to initialize a Kubernetes-focused AI agent with Google ADK.
