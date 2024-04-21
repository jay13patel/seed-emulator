# CARLA-SEED Co-Drive


This manual provides comprehensive guidance on setting up, operating, and optimizing Carla-Seed Co-Drive, ensuring you efficiently leverage both simulation and emulation to enhance your projects. From installation to advanced features, find all the information you need to effectively navigate and utilize this integrated platform.

## What is CARLA Simulator

CARLA Simulator is an open-source platform designed specifically for the development and testing of autonomous driving systems. It uses Unreal Engine, known for its powerful rendering capabilities, to create highly realistic urban environments. This allows researchers and developers to simulate and analyze various scenarios that autonomous vehicles might encounter. CARLA supports the ASAM OpenDRIVE standard to define roads and traffic settings, ensuring the environments are accurate and detailed.

The architecture of CARLA is based on a client-server model. The server manages the core simulation tasks, including the rendering of sensors, physics calculations, and maintaining the state of the world and its actors. This setup is ideal for achieving realistic results, especially when paired with a dedicated GPU to handle the intensive computations. On the client side, users interact with the simulation through a flexible API available in Python and C++. This API allows users to control vehicle behaviors, set environmental conditions, and integrate with external systems for more complex simulations.

In essence, CARLA provides a comprehensive toolkit for anyone looking to advance the field of autonomous driving, offering tools for scenario creation, data collection, and system validation. Its open-source nature also encourages collaboration and innovation, making it a central hub for autonomous vehicle research.

## Key Components of CARLA

### CARLA Server/World

DNS infrastructure is required for the PKI infrastructure to work. The PKI infrastructure will consult the DNS infrastructure to resolve the domain names and verify the target node's control of domain in ACME challenges.

### CARLA Client
To create a PKI infrastructure, we need to prepare the Root CA store. The Root CA store is abstracted as a class but it is essentially a folder living in the host machine's `/tmp` directory. The Root CA store is used to generate the corresponding Root CA certificate and private key at the build time. It is also possible to supply your own Root CA certificate and private key.

### Traffic Manager

In this example, we use a web server to demonstrate how the PKI is used. 
This is a simple web server that serves a static page. When this machine starts,
it will request a certificate from the specified CA server, and use it to serve HTTPS requests.

### Synchronous and asynchronous mode

### Sensors


## CARLA Simulator + SEED Emulator 

### Integration Architecture

### System Requirements 

### CARLA Simulator Installation

### SEED Emulator Installation

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

