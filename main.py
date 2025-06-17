import asyncio
from aiocoap import *

async def main():
    context = await Context.create_client_context()

    request = Message(code=GET, uri='coap://californium.eclipseprojects.io/.well-known/core')

    try:
        response = await context.request(request).response
        print("Response Code:", response.code)
        print("Available Resources:")
        print(response.payload.decode('utf-8'))
    except Exception as e:
        print("Failed to fetch resources:", e)

asyncio.run(main())