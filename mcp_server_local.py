from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    "Weather",
    instructions="You are a weather tool that can get the weather in a given city",
    host="0.0.0.0",
    port=8005
)

@mcp.tool()
async def get_weather(city: str) -> str:
    """Get the weather in a given city"""
    return f"The weather in {city} is 흐림"

if __name__ == "__main__":
    mcp.run(transport="stdio")