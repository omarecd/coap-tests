import asyncio
import aiocoap

async def main():
    context = await aiocoap.Context.create_client_context()
    request = aiocoap.Message(code=aiocoap.GET, uri='coap://californium.eclipseprojects.io/test')

    try:
        response = await context.request(request).response
        print("Response Code:", response.code)
        print("Value from /obs:")
        print(response.payload.decode('utf-8'))
    except Exception as e:
        print("Error:", e)

asyncio.run(main())