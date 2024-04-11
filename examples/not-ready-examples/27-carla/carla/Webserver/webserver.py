import argparse
import asyncio
import websockets
import json
import carla


parser = argparse.ArgumentParser(description='Webserver for handling CARLA vehicle commands.')
parser.add_argument('--ws_ip', default='localhost', help='IP address for the WebSocket server.')
parser.add_argument('--ws_port', type=int, default=6789, help='Port number for the WebSocket server.')

args = parser.parse_args()

connected_clients = set()
monitor_clients = set()


    
async def handle_client(websocket, path):
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

