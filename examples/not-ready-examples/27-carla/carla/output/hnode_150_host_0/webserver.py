import argparse
import asyncio
import websockets
import json
import carla


parser = argparse.ArgumentParser(description='Webserver for handling CARLA vehicle commands.')
parser.add_argument('--ws_ip', default='localhost', help='IP address for the WebSocket server.')
parser.add_argument('--ws_port', type=int, default=6789, help='Port number for the WebSocket server.')
parser.add_argument('--carla_ip', default='127.0.0.1', help='IP address of the CARLA server.')
parser.add_argument('--carla_port', type=int, default=2000, help='Port number of the CARLA server.')
args = parser.parse_args()

connected_clients = set()
monitor_clients = set()

client = carla.Client(args.carla_ip, args.carla_port)  # Adjust IP and port if needed
client.set_timeout(60.0)
world = client.get_world()
    
async def handle_client(websocket, path):
    global world
    vehicle_actors = world.get_actors().filter('vehicle.*')

    for vehicle in vehicle_actors:
        role_name = vehicle.attributes.get('role_name', 'Unknown')
        #print(f"Vehicle {vehicle.id} with role: {role_name}")
    connected_clients.add(websocket)
    try:
        if websocket.open:
            print("Client connected.")
            async for message in websocket:
                data = json.loads(message)
                if data["type"] == "set_destination":
                # Prepare the list of tasks for broadcasting the message
                    tasks = [client.send(message) for client in connected_clients if client != websocket]
                # Check if there are tasks to execute
                    if tasks:
                        await asyncio.wait(tasks)
                    else:
                        print("No other connected clients to send the message to.")
                elif data["type"] == "destination_reached":
                    notification = json.dumps(data)  # Check if there are any monitor clients connected
                    print("Webserver packet recive")
                    await asyncio.wait([client.send(notification) for client in connected_clients])
        else:
            print("Websocket connection closed. Cannot send message")

    except websockets.exceptions.ConnectionClosedOK:
        print("Attempted to send a message, but connection was closed normally.")
    except websockets.exceptions.ConnectionClosedError:
        print("Client disconnected unexpectedly.")
    except websockets.exceptions.WebSocketException as e:
        print(f"An error occurred while sending a message: {e}")
    finally:
        connected_clients.remove(websocket)
        monitor_clients.discard(websocket)


start_server = websockets.serve(handle_client, args.ws_ip, args.ws_port)
asyncio.get_event_loop().run_until_complete(start_server)
try:
    asyncio.get_event_loop().run_forever()
except KeyboardInterrupt:
    print("Program terminated by user")

