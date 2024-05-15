import asyncio
import websockets
from aiohttp import web

# Init client
connected_web_clients = set()

# Init variable for messages
messages = []

# Function broadcast_message that sends message to all connected web clients in set
async def broadcast_message(message):
    # Prepare a WebSocket text message with the new message
    websockets.broadcast(connected_web_clients, message)

# Function websocket_handler to append received message to list messages
async def websocket_handler(websocket):
    connected_web_clients.add(websocket)
    try:
        async for message in websocket:
            # Append each received message to the list
            messages.append(message)
            await broadcast_message(message)
    finally:
        connected_web_clients.remove(websocket)

# Function web_handler that asynchronously builds index.html 
# and updates it with each new received message
async def web_handler(request):
    #sub var ws values for docker: host.docker.internal, k8s: localhost
    return web.Response(text='''
        <html>
        <head><title>ML Infrastructure HW</title></head>
        <body>
            <h1>Messages received:</h1>
            <ul id="messages"></ul>
            <script>
                var ws = new WebSocket('ws://localhost:65432');
                ws.onmessage = function(event) {
                    var messages = document.getElementById('messages');
                    var message = document.createElement('li');
                    message.textContent = event.data;
                    messages.appendChild(message);
                };
            </script>
        </body>
        </html>
    ''', content_type='text/html')

# Function server that inits simple HTTP server using python utilizing AIOHTTP
async def server():
    # Setup websocket server endpoint; using 0.0.0.0 as addr for k8s
    ws_server = websockets.serve(websocket_handler, '0.0.0.0', 65432)

    # Setup AIOHTTP web server
    app = web.Application()
    app.add_routes([web.get('/', web_handler)])
    runner = web.AppRunner(app)
    await runner.setup()
    # Utilize 0.0.0.0 as addr for k8s
    site = web.TCPSite(runner, '0.0.0.0', 8081)
    await site.start()

    # Run both servers indefinitely
    await asyncio.gather(ws_server, asyncio.Future())
    