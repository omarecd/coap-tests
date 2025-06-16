import asyncio
from aiocoap import *

async def main():
    context = await Context.create_client_context()

    request = Message(code=GET, uri='coap://californium.eclipseprojects.io/obs')

    try:
        response = await context.request(request).response
        print("Response Code:", response.code)
        print("Value from /obs:")
        print(response.payload.decode('utf-8'))
    except Exception as e:
        print("Error:", e)

asyncio.run(main())