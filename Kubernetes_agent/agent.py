import asyncio
import os
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters
from .prompts import return_instructions_root


async def get_tools_async():
        
        """
        Asynchronously start the MCP server and retrieve the available tools.

        Uses npx to launch the `mcp-server-kubernetes` process and
        establishes a stdio connection to obtain the MCPToolset.

        Returns:
            tools (list): Discovered MCP tools for Kubernetes operations.
            exit_stack: Context manager for cleaning up the server connection.
        """

        tools, exit_stack = await MCPToolset.from_server(
            connection_params=StdioServerParameters(
                command='npx',
                args=["mcp-server-kubernetes"],
            )
        )
        print(f"--- Successfully connected to k8s server Discovered {len(tools)} tool(s). ---")
        for tool in tools:
            print(f"  - Discovered tool: {tool.name}") 
        return tools, exit_stack


async def create_agent():

    """
    Construct the Kubernetes MCP Agent.

    Workflow:
      1. Load environment variables from `.env` (e.g., credentials).
      2. Discover available MCP tools using `get_tools_async()`.
      3. Fetch the instruction prompt from `return_instructions_root()`.
      4. Instantiate and return the Agent.

    Returns:
        agent_instance (Agent): Configured AI agent for Kubernetes tasks.
        exit_stack: Cleanup context for tool connections.
    """

    tools, exit_stack = await get_tools_async()
    if not tools:
        print("no tools")

    agent_instance = Agent(
        name= "kubernetes_MCP",
        description= "Kuberntes MCP Agent",
        model= 'gemini-2.5-flash-preview-05-20',
        instruction=return_instructions_root(),
                   
        tools=tools, 

    )
    return agent_instance, exit_stack

# Initialize the root agent (returns a coroutine)
root_agent= create_agent()