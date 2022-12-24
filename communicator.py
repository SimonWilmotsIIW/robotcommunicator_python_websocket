#!/usr/bin/env python

import asyncio
import websockets
import json

async def communicator(websocket):
    command = await websocket.recv()
    data = json.loads(command)
    coordinates = data["coordinates"]
    print("<<< Received: " + command)


    await websocket.send(json.dumps(coordinates))
    print(f">>> {coordinates}")

async def main():
    async with websockets.serve(communicator, "localhost", 8765):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())