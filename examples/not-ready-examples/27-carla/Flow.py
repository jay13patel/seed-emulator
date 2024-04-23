

from graphviz import Digraph

# Initialize a new directed graph
flow = Digraph(comment='Initialization Flow')

# Define the nodes
flow.node('A', 'Car 1\nautomatic.control.py')
flow.node('B', 'Carla World\nInternet Exchange')
flow.node('C', 'Internet Router')
flow.node('D', 'CARLA Server\n(Remote)')
flow.node('E', 'WebSocket')
flow.node('F', 'Controller')
flow.node('G', 'World\nSensory Feed')

# Define the edges
flow.edge('A', 'B', 'Connect Request')
flow.edge('B', 'C', 'To Internet Router')
flow.edge('C', 'D', 'To Remote Server')
flow.edge('A', 'E', 'WebSocket Connect')
flow.edge('F', 'E', 'Send Instructions')
flow.edge('D', 'A', 'Deploy Confirmation')
flow.edge('G', 'A', 'Sensory Data')
flow.edge('A', 'D', 'Decision Making (e.g., Stop at red light)')

# Render the graph to a file and show the output file path
flow.render('/home/kkshaikh/carla-seed/seed-emulator/examples/not-ready-examples/27-carla/initialization_flow', format='png', cleanup=True)

# Output the file path to access the diagram
'/home/kkshaikh/carla-seed/seed-emulator/examples/not-ready-examples/27-carla/initialization_flow.png'