# Now you have seen the server is created in teh 01_mcp_server.py file but its just a server we need a client
# That actually calls tools show user friendly ui and server will communicate trough it 

import os 
from mcp.client import stdio
from mcp import ClientSession, StdioServerParameters, Client

# Path to our MCP server script 
