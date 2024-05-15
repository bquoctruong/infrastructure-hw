import asyncio
import websockets
import random
import time

# Function client that sends message "Hello, Server!" to server listed in URI
async def client():
    # Sub var ws values for docker: host.docker.internal, k8s: websocket-server-service
    uri = "ws://websocket-server-service:65432"
    async with websockets.connect(uri) as websocket:
        while True:
            # Send server message
            message = "Hello, Server!"
            await websocket.send(message)
            print(f"Sent: {message}")

            # Sleep for random time between 1-10 seconds
            await asyncio.sleep(random.randint(1, 10))  