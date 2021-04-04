from aiohttp_json_rpc import JsonRpcClient
import asyncio

async def ping_json_rpc():
    """Connect to ws://localhost:8080/, call ping() and disconnect."""
    rpc_client = JsonRpcClient()
    try:
        await rpc_client.connect('localhost', 8080)
        call_result = await rpc_client.call('send', params={'mod': 'http', 'url':'google.com', 'method':'get'})
        print(call_result)  # prints 'pong' (if that's return val of ping)
    finally:
        await rpc_client.disconnect()


asyncio.get_event_loop().run_until_complete(ping_json_rpc())