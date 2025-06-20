#get_test_value_from_eclipse.py
# This script retrieves a test value from the Eclipse Californium CoAP server.
# It uses the aiocoap library to send a GET request to the server and prints the response.

import asyncio
import aiocoap

async def main():
    context = await aiocoap.Context.create_client_context()
    request = aiocoap.Message(code=aiocoap.GET, uri='coap://californium.eclipseprojects.io/obs')
    #request = aiocoap.Message(code=aiocoap.GET, uri='coap://californium.eclipseprojects.io/test')
    #request = aiocoap.Message(code=aiocoap.GET, uri='coap://californium.eclipseprojects.io/echo/cali.Ali.LAR91X')
    #request = aiocoap.Message(code=aiocoap.GET, uri='coap://californium.eclipseprojects.io/obs-pumping')
    #request = aiocoap.Message(code=aiocoap.GET, uri='coap://californium.eclipseprojects.io/obs-large')

    try:
        response = await context.request(request).response
        print("Response Code:", response.code)
        print("Value from /obs:")
        print(response.payload.decode('utf-8'))
    except Exception as e:
        print("Error:", e)

asyncio.run(main())