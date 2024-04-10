#!/usr/bin/env python3
import argparse
import carla
import asyncio
import websockets
import json
import math


parser = argparse.ArgumentParser(description=" Get your car information")
parser.add_argument("--carla_ip", default="localhost", help="IP address of the CARLA server")
parser.add_argument("--carla_port", default=2000, type=int, help="Port number of the CARLA server")
parser.add_argument("--car_info", help="Get detailed info for a car based on its role name")

args = parser.parse_args()

async def get_vehicle_info(role_name):
    client = carla.Client(args.carla_ip, args.carla_port)
    client.set_timeout(10.0)
    world = client.get_world()   
    try:
        while True:
            vehicle_actors = world.get_actors().filter('vehicle.*')
            found = False
            for vehicle in vehicle_actors:
                # Check if the vehicle matches the specified role name
                if vehicle.attributes.get('role_name', '') == role_name:
                    # Get vehicle location
                    location = vehicle.get_location()
                    location_str = f"({location.x:.2f}, {location.y:.2f}, {location.z:.2f})"
                    
                    # Get vehicle speed (in km/h)
                    velocity = vehicle.get_velocity()
                    speed_kmh = 3.6 * math.sqrt(velocity.x**2 + velocity.y**2 + velocity.z**2)  # Convert m/s to km/h
                    controls = vehicle.get_control()
                    
                    # Get the vehicle type (model)
                    car_type = vehicle.type_id

                    print(f"Vehicle ID: {vehicle.id} with role: {role_name}")
                    print(f"Location: {location_str}")
                    print(f"Speed: {speed_kmh:.2f} km/h")
                    print(f"Car Type: {car_type}")
                    print(f"Throttle: {controls.throttle:.2f},\nBrake: {controls.brake:.2f},\nSteer: {controls.steer:.2f},\nReverse: {controls.reverse},\nHand Brake: {controls.hand_brake}\n")
                    found = True

                    # Assuming you only need info for the first vehicle that matches the role name
                    break
            if not found:
                # This else block executes if no vehicle matching the role name is found in the loop
                print(f"No vehicle found with role name: {role_name}")
            
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        print("Program terminated by user")

if __name__ == "__main__":
    if args.car_info:
        try:
            asyncio.get_event_loop().run_until_complete(get_vehicle_info(args.car_info))
            exit()
        except KeyboardInterrupt:
            print("Program terminated by user. Exiting gracefully.")
            exit(0)

