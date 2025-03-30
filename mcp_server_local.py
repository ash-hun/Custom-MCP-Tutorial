from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    "Information",
    instructions="You are a information tool that can get the color or name in a given target",
    host="0.0.0.0",
    port=8005
)

@mcp.tool()
async def get_color(target: str) -> str:
    """Get the color in a given target"""
    return f"{target}'s color is BLUE"

@mcp.tool()
async def get_name(target: str) -> str:
    """Get the weather in a given city"""
    return f"{target}'s name is ASH"

if __name__ == "__main__":
    mcp.run(transport="sse")
    # mcp.run(transport="stdio")