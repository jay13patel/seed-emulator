#!/usr/bin/env python3
# encoding: utf-8

from seedemu import *


###############################################################################
emu     = Emulator()
base    = Base()
routing = Routing()
ebgp    = Ebgp()
ibgp    = Ibgp()
ospf    = Ospf()
web     = WebService()
ovpn    = OpenVpnRemoteAccessProvider()


###############################################################################

ix100 = base.createInternetExchange(100)
#ix101 = base.createInternetExchange(101)
#ix102 = base.createInternetExchange(102)
#ix103 = base.createInternetExchange(103)
#ix104 = base.createInternetExchange(104)
#ix105 = base.createInternetExchange(105)

# Customize names (for visualization purpose)
ix100.getPeeringLan().setDisplayName('Carla-World')
#ix101.getPeeringLan().setDisplayName('San Jose-101')
#ix102.getPeeringLan().setDisplayName('Chicago-102')
#ix103.getPeeringLan().setDisplayName('Miami-103')
#ix104.getPeeringLan().setDisplayName('Boston-104')
#ix105.getPeeringLan().setDisplayName('Huston-105')

'''
###############################################################################
# Create Transit Autonomous Systems 

## Tier 1 ASes
Makers.makeTransitAs(base, 2, [100, 101, 102, 105], 
       [(100, 101), (101, 102), (100, 105)] 
)

Makers.makeTransitAs(base, 3, [100, 103, 104, 105], 
       [(100, 103), (100, 105), (103, 105), (103, 104)]
)

Makers.makeTransitAs(base, 4, [100, 102, 104], 
       [(100, 104), (102, 104)]
)

## Tier 2 ASes
Makers.makeTransitAs(base, 11, [102, 105], [(102, 105)])
Makers.makeTransitAs(base, 12, [101, 104], [(101, 104)])

'''
###############################################################################
# Create single-homed stub ASes. "None" means create a host only 

Makers.makeStubAs(emu, base, 150, 100, [None])
Makers.makeStubAs(emu, base, 151, 100, [None])

Makers.makeStubAs(emu, base, 152, 100, [None])
Makers.makeStubAs(emu, base, 153, 100, [None])

Makers.makeStubAs(emu, base, 154, 100, [None])
Makers.makeStubAs(emu, base, 155, 100, [None])

Makers.makeStubAs(emu, base, 156, 100, [None])
Makers.makeStubAs(emu, base, 157, 100, [None])
Makers.makeStubAs(emu, base, 158, 100, [None])

'''

as150 = base.createAutonomousSystem(150)
as150.createNetwork('net0')
as150.createRouter('router0').joinNetwork('net0').joinNetwork('ix100')

as151 = base.createAutonomousSystem(151)
as151.createNetwork('net0')
as151.createRouter('router0').joinNetwork('net0').joinNetwork('ix100')

as152 = base.createAutonomousSystem(152)
as152.createNetwork('net0')
as152.createRouter('router0').joinNetwork('net0').joinNetwork('ix100')

as153 = base.createAutonomousSystem(153)
as153.createNetwork('net0')
as153.createRouter('router0').joinNetwork('net0').joinNetwork('ix100')

as154 = base.createAutonomousSystem(154)
as154.createNetwork('net0')
as154.createRouter('router0').joinNetwork('net0').joinNetwork('ix100')


as155 = base.createAutonomousSystem(155)
as155.createNetwork('net0')
as155.createRouter('router0').joinNetwork('net0').joinNetwork('ix100')

as156 = base.createAutonomousSystem(156)
as156.createNetwork('net0')
as156.createRouter('router0').joinNetwork('net0').joinNetwork('ix100')

as157 = base.createAutonomousSystem(157)
as157.createNetwork('net0')
as157.createRouter('router0').joinNetwork('net0').joinNetwork('ix100')

as158 = base.createAutonomousSystem(158)
as158.createNetwork('net0')
as158.createRouter('router0').joinNetwork('net0').joinNetwork('ix100')
'''

# Create real-world AS.
# AS11872 is the Syracuse University's autonomous system

as11872 = base.createAutonomousSystem(11872)
as11872.createRealWorldRouter('rw-11872-syr').joinNetwork('ix100', '10.100.0.95')


###############################################################################
# Create hybrid AS.
# AS99999 is the emulator's autonomous system that routes the traffics to the real-world internet
as99999 = base.createAutonomousSystem(99999)
as99999.createRealWorldRouter('rw-real-world', prefixes=['0.0.0.0/1', '128.0.0.0/1', '10.0.0.0/1']).joinNetwork('ix100', '10.100.0.99')
###############################################################################


###############################################################################
# Peering via RS (route server). The default peering mode for RS is PeerRelationship.Peer, 
# which means each AS will only export its customers and their own prefixes. 
# We will use this peering relationship to peer all the ASes in an IX.
# None of them will provide transit service for others. 

#ebgp.addRsPeers(100, [2, 3, 4])
#ebgp.addRsPeers(102, [2, 4])
#ebgp.addRsPeers(104, [3, 4])
#ebgp.addRsPeers(105, [2, 3])


ebgp.addRsPeer(100, 150)
ebgp.addRsPeer(100, 151)
ebgp.addRsPeer(100, 152)
ebgp.addRsPeer(100, 153)
ebgp.addRsPeer(100, 154)
ebgp.addRsPeer(100, 155)
ebgp.addRsPeer(100, 156)
ebgp.addRsPeer(100, 157)
ebgp.addRsPeer(100, 158)
ebgp.addRsPeer(100, 99999)


'''
# To buy transit services from another autonomous system, 
# we will use private peering  

ebgp.addPrivatePeerings(100, [2],  [150, 151], PeerRelationship.Provider)
ebgp.addPrivatePeerings(100, [3],  [150, 99999], PeerRelationship.Provider)

ebgp.addPrivatePeerings(101, [2],  [12], PeerRelationship.Provider)
ebgp.addPrivatePeerings(101, [12], [152, 153], PeerRelationship.Provider)

ebgp.addPrivatePeerings(102, [2, 4],  [11, 154], PeerRelationship.Provider)
ebgp.addPrivatePeerings(102, [11], [154, 11872], PeerRelationship.Provider)

ebgp.addPrivatePeerings(103, [3],  [160, 161, 162 ], PeerRelationship.Provider)

ebgp.addPrivatePeerings(104, [3, 4], [12], PeerRelationship.Provider)
ebgp.addPrivatePeerings(104, [4],  [163], PeerRelationship.Provider)
ebgp.addPrivatePeerings(104, [12], [164], PeerRelationship.Provider)

ebgp.addPrivatePeerings(105, [3],  [11, 170], PeerRelationship.Provider)
ebgp.addPrivatePeerings(105, [11], [171], PeerRelationship.Provider)

'''
###############################################################################

# Add layers to the emulator
emu.addLayer(base)
emu.addLayer(routing)
emu.addLayer(ebgp)
emu.addLayer(ibgp)
emu.addLayer(ospf)
emu.addLayer(web)


# Save it to a component file, so it can be used by other emulators
emu.dump('base-component.bin')

# Uncomment the following if you want to generate the final emulation files
emu.render()
#print(dns.getZone('.').getRecords())
emu.compile(Docker(), './output', override=True)

