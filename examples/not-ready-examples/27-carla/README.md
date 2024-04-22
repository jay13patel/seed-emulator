# CARLA-SEED Co-Drive

This manual provides comprehensive guidance on setting up, operating, and optimizing Carla-Seed Co-Drive, ensuring you efficiently leverage both simulation and emulation to enhance your projects. From installation to advanced features, find all the information you need to effectively navigate and utilize this integrated platform.
## What is CARLA Simulator

CARLA Simulator is an open-source platform designed specifically for the development and testing of autonomous driving systems. It uses Unreal Engine, known for its powerful rendering capabilities, to create highly realistic urban environments. This allows researchers and developers to simulate and analyze various scenarios that autonomous vehicles might encounter.

Read More: https://carla.readthedocs.io/en/latest/start_introduction/

## Key Components of CARLA Simulator

The architecture of CARLA is based on a client-server model.

![[Pasted image 20240421184832.png]]
### CARLA Server/World

In the CARLA Simulator setup, the server handles all the core tasks necessary for the simulation. This includes rendering the sensors, computing the physics to ensure realistic interactions within the simulated world, and updating the state of the world and its various actors. Given the demand for high-quality, realistic outputs, the server ideally runs on a dedicated GPU. This setup is particularly important as it helps in efficiently managing intensive tasks, thereby enhancing the fidelity and responsiveness of the simulation.
### CARLA Client

CARLA clients represent the entities interacting with the simulation environment. These clients can be autonomous vehicles, Python programs, or any other entities controlling the logic of actors within the scene and setting world conditions. Leveraging the CARLA API, available in Python or C++, these clients communicate with the server to influence the simulation.

Read More: https://carla.readthedocs.io/en/latest/foundations/#world-and-client

## CARLA Simulator + SEED Emulator 

### Integration Architecture

### CARLA Simulator Installation

#### System Requirements for Carla Server
- **Operating Systems:** Windows, Linux
- **CPU:** Quad-core Intel or AMD, 2.5 GHz or faster
- **RAM (Memory):** 
	- Minimum: 16 GB 
	- Recommended: 32 GB for optimal performance
- **GPU:**
    - Minimum: 6 GB RAM
    - Recommended: 8 GB RAM for optimal performance
    - Note: Dedicated GPU strongly recommended for machine learning
- **Disk Space:** 20 GB free space
- **Python:** Version 3.7 supported on both Windows and Linux
- **Pip:** Version 20.3 or higher
- **Network:** TCP ports 2000 and 2001 must be open

#### Windows Installation
1. **Visit the CARLA GitHub Page:**
    - Go to [CARLA GitHub Page](https://github.com/carla-simulator/carla/blob/master/Docs/download.md).
2. **Locate the Windows:**
    
    - Find and click on the link for the Windows version of CARLA.
3. **Download and Unzip:**
    
    - Download the CARLA package for Windows.
    - Once downloaded, unzip the file to extract its contents.
4. **Install pip3:**
    
    - Open Command Prompt as an administrator.
    - Run the command  `pip3 install --user pygame numpy` to install Pygame and NumPy.
    - Additionally, install CARLA python package run this command `pip3 install carla`.
5. **Navigate to CARLA Root Directory:**
    
    - Open Command Prompt.
    - Use the `cd` command to navigate to the directory where CARLA was extracted. For example:
        
        bashCopy code
        
        `cd path\to\carla\root`
        
6. **Launch CARLA:**
    
    - Run the command `CarlaUE4.exe` to start CARLA.
    - A window will appear displaying a view of the city. This is the spectator view.
    - To navigate around the city, use the mouse and WASD keys. Hold down the right mouse button to control the direction.



### SEED Emulator Installation

one

### Usage 
### Integration Features

#### Simulation Controls

#### Data Exchange

#### Visualizations

### Troubleshooting

#### Common Issues

A list of common problems that may arise when using the integration and their solutions.
#### Debugging Tips 

Tips for diagnosing and fixing issues specific to the integration

