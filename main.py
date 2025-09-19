#!/usr/bin/env python3
import os
import requests
from fastmcp import FastMCP

# Get LinkedIn token from environment
LINKEDIN_TOKEN = os.environ.get("LINKEDIN_ACCESS_TOKEN", "")

# Create the MCP server
mcp = FastMCP(
    name="LinkedIn MCP",
    instructions="I help you post to LinkedIn and manage your professional presence."
)

@mcp.tool()
async def test_connection() -> dict:
    """Test the MCP server connection"""
    return {
        "status": "Connected!",
        "message": "MCP server is working",
        "linkedin_configured": bool(LINKEDIN_TOKEN)
    }

@mcp.tool()
async def linkedin_post(text: str) -> dict:
    """Post to LinkedIn"""
    if not LINKEDIN_TOKEN:
        return {"error": "LinkedIn token not configured"}
    
    # Add your LinkedIn API implementation here
    return {
        "success": True,
        "message": f"Ready to post: {text[:100]}..."
    }

if __name__ == "__main__":
    # Use environment variable for port (Railway/Render will set this)
    port = int(os.environ.get("PORT", 3000))
    mcp.run(transport="sse", host="0.0.0.0", port=port)
