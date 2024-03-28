#!/bin/env python3 

import math
from .MobilityModel import *
import time

class StarMobilityHelper():
    isPaused:bool
    position:Vector
    radius:float
    maxRadius:float
    lastUpdate:float
    nodeId:int
    nodeTotal:int
    
    def __init__(self, nodeId, nodeTotal, centerX, centerY, radius=None, maxRadius=None, paused=True):
        self.nodeId=nodeId
        self.nodeTotal = nodeTotal
        self.radius=radius
        self.maxRadius=maxRadius
        self.isPaused = paused
        self.centerX = centerX
        self.centerY = centerY
        self.position = self.calculateStarPosition()

    def getPosition(self):
        return self.position
    
    def setPosition(self, position):
        self.position = position
    
    def setMaxRadius(self, maxRadius):
        self.maxRadius = maxRadius
        self.lastUpdate = time.time()
    
    def updatePosition(self, isRealtime:bool=False, deltaS:int = 1):
        now = time.time()
        
        if self.isPaused:
            return
        
        if isRealtime:
            if now - self.lastUpdate < 1:
                return
            deltaS = round(now - self.lastUpdate)
        else:
            # SeedSimLogger.debug(clsname=__name__, msg="deltaS = 1")
            deltaS = deltaS

        if not self.isPaused:
            self.lastUpdate = now
            self.radius += 5 * deltaS

            if self.radius > self.maxRadius:
                return
            else:
                self.position = self.calculateStarPosition()

    def pause(self):
        self.isPaused = True
        return self
    
    def unpause(self):
        self.isPaused = False
        return self
    
    def calculateStarPosition(self):
        if self.nodeId == 0:
            return Vector(round(self.centerX,2), round(self.centerY,2), 0)
        theta = 2 * math.pi * self.nodeId / (self.nodeTotal-1)
        x = self.centerX + self.radius * math.cos(theta)
        y = self.centerY + self.radius * math.sin(theta)
        return Vector(round(x,2), round(y,2), 0)

class StarMobilityModel(MobilityModel):
    helper:StarMobilityHelper

    def __init__(self, nodeId, nodeTotal, centerX, centerY, radius, maxRadius=None):
        self.helper = StarMobilityHelper(nodeId=nodeId, nodeTotal=nodeTotal, centerX=centerX, centerY=centerY, radius=radius)
        if maxRadius is not None:
            self.setMaxRadius(maxRadius)
        super().__init__(self.helper.getPosition())
        

    def doGetVelocity(self):
        return Vector(0.0, 0.0, 0.0)
    
    def doUpdatePosition(self):
        return self.helper.updatePosition(deltaS=self.deltaS)

    def doGetPosition(self):
        # self.helper.updatePosition(self.boundary, self.isBouncy)
        return self.helper.getPosition()
    
    def doSetPosition(self, position):
        self.helper.setPosition(position)
    
    def setMaxRadius(self, maxRadius):
        self.helper.setMaxRadius(maxRadius)
        self.helper.unpause()
        return self