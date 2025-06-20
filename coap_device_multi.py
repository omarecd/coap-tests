# coap_device_multi.py
import asyncio
import random
import sys
from aiocoap import resource, Message, Context
from aiocoap.numbers.codes import Code

class TemperatureResource(resource.Resource):
    async def render_get(self, request):
        temperature = round(random.uniform(20.0, 30.0), 2)
        payload = f"{temperature} °C".encode("utf-8")
        return Message(code=Code.CONTENT, payload=payload)

async def main(port):
    root = resource.Site()
    root.add_resource(['temperature'], TemperatureResource())

    print(f"🌡️ CoAP device running on 127.0.0.1:{port} (/temperature)")
    await Context.create_server_context(root, bind=('127.0.0.1', port))
    await asyncio.get_running_loop().create_future()

if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 5683
    asyncio.run(main(port))