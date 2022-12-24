#!/usr/bin/env python

import asyncio
import websockets
import random
import uuid
import json

async def setup_robot():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        name = str(input("Robot name: "))
        robot_id = str(uuid.uuid4())
        print("*** Move robot to coordinates ***")
        x = str(input("x: "))
        y = str(input("y: "))
        z = str(input("z: "))

        command = '{ "id": "' + robot_id + '", "name": "' + name + '", "coordinates": { "x": '+ x +', "y": ' + y + ', "z": ' + z + ' }}'
        
        await websocket.send(command)
        print(f">>>>>> {robot_id}, {name}, x: {x}, y: {y}, z: {z}")

        data = await websocket.recv()
        json_data = json.loads(data)
        # Hier kan de robot dan aangestuurd worden met ROS of een ander ROBOTICS framework :)
        print("Received movement commands:")
        for key, value in json_data.items():
            print(key + ": ", value)


if __name__ == "__main__":
    asyncio.run(setup_robot())