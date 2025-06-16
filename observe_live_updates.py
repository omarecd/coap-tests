import asyncio
from aiocoap import *

async def main():
    context = await Context.create_client_context()

    request = Message(code=GET, uri='coap://californium.eclipseprojects.io/obs', observe=0)

    try:
        protocol_request = context.request(request)

        async for response in protocol_request.observation:
            print("🔄 New update received:")
            print(response.payload.decode('utf-8'))
    except Exception as e:
        print("❌ Error:", e)

asyncio.run(main())