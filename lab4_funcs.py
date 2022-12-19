#!/usr/bin/python
# -*- coding: UTF-8 -*-

from lab4_swarm import Swarm
import numpy as np

class Swarm_X2(Swarm):
    def __init__ (self, swarmsize, minvalues, maxvalues, currentVelocityRatio, localVelocityRatio, globalVelocityRatio):
       super().__init__ (swarmsize, minvalues, maxvalues, currentVelocityRatio, localVelocityRatio, globalVelocityRatio)

    @staticmethod
    def fun(x1,x2):
        return x1**2 + x2**2

    def _finalFunc (self, position):
        penalty = self._getPenalty (position, 10000.0)
        finalfunc = sum (position * position)

        return finalfunc + penalty

    def graph(self):
        x1 = np.linspace(-100, 100, 100)
        x2 = np.linspace(-100, 100, 100)
        x1,x2 = np.meshgrid(x1, x2)
        f = np.array([Swarm_X2.fun(x1[i],x2[i]) for i in range(len(x1))])
        return x1,x2,f


class Swarm_Schwefel (Swarm):
    def __init__ (self, 
            swarmsize, 
            minvalues, 
            maxvalues, 
            currentVelocityRatio,
            localVelocityRatio, 
            globalVelocityRatio):
       Swarm.__init__ (self, 
            swarmsize, 
            minvalues, 
            maxvalues, 
            currentVelocityRatio,
            localVelocityRatio, 
            globalVelocityRatio)


    def _finalFunc (self, position):
        function = sum (-position * np.sin (np.sqrt (np.abs (position) ) ) )
        penalty = self._getPenalty (position, 10000.0)
        return function + penalty

    @staticmethod
    def fun(x1,x2):
        return -x1*np.sin(np.sqrt(np.fabs(x1))) - x2*np.sin(np.sqrt(np.fabs(x2)))

    def graph(self):
        x1 = np.linspace(-500, 500, 200)
        x2 = np.linspace(-500, 500, 200)
        x1,x2 = np.meshgrid(x1, x2)
        f = np.array([Swarm_Schwefel.fun(x1[i],x2[i]) for i in range(len(x1))])
        return x1,x2,f



class Swarm_Rastrigin(Swarm):
    def __init__ (self, 
            swarmsize, 
            minvalues, 
            maxvalues, 
            currentVelocityRatio,
            localVelocityRatio, 
            globalVelocityRatio):
       Swarm.__init__ (self, 
            swarmsize, 
            minvalues, 
            maxvalues, 
            currentVelocityRatio,
            localVelocityRatio, 
            globalVelocityRatio)


    def _finalFunc (self, position):
        function = 10.0 * len (self.minvalues) + sum (position * position - 10.0 * np.cos (2 * np.pi * position) )
        penalty = self._getPenalty (position, 10000.0)

        return function + penalty

    @staticmethod
    def fun(x1,x2):
        return 20 + x1**2 - 10*np.cos(2*np.pi*x1) + x2**2 - 10*np.cos(2*np.pi*x2)

    def graph(self):
        x1 = np.linspace(-5.5, 5.5, 100)
        x2 = np.linspace(-5.5, 5.5, 100)
        x1,x2 = np.meshgrid(x1, x2)
        f = np.array([Swarm_Rastrigin.fun(x1[i],x2[i]) for i in range(len(x1))])
        return x1,x2,f
