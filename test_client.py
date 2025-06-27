import asyncio
from fastmcp import Client

async def main():
    async with Client("http://127.0.0.1:8000/sse") as client:
        print("Available tools:", await client.list_tools())
        print(await client.call_tool("start_presentation", {}))
        await asyncio.sleep(2)
        print(await client.call_tool("next_slide", {}))
        await asyncio.sleep(1)
        print(await client.call_tool("previous_slide", {}))
        await asyncio.sleep(1)
        print(await client.call_tool("go_to_slide", {"slide_number": 3}))
        await asyncio.sleep(1)
        print(await client.call_tool("end_presentation", {}))

if __name__ == "__main__":
    asyncio.run(main()) 