#! /bin/env python3
from pylab import *

def velocity(r, b):
  return r*exp((1. - r**b)/b)

npc = genfromtxt('data/grassi_npc.csv', delimiter = ',')
spc = genfromtxt('data/grassi_spc.csv', delimiter = ',')

rnp, vnp = 1000, 75
rsp, vsp = 1200, 80

rr = linspace(0, 5000, 100)

figure(1, figsize = (6,6))
ax = axes()
ax.step(npc[:,0], npc[:,1], 'k', linewidth = 3)
ax.plot(rr, vnp*velocity(rr/rnp, 1.), '--', color = '0.1', label = 'b=1')
ax.plot(rr, vnp*velocity(rr/rnp, 1.5), '-', color = '0.1', label = 'b=1.5')
ax.plot(rr, vnp*velocity(rr/rnp, 2.), '-.', color = '0.1', label = 'b=2')

ax.step(spc[:,0], spc[:,1], 'k', linewidth = 3)
ax.plot(-rr, vsp*velocity(rr/rsp, 1.), '--', color = '0.1')
ax.plot(-rr, vsp*velocity(rr/rsp, 1.5), '-', color = '0.1')
ax.plot(-rr, vsp*velocity(rr/rsp, 2.), '-.', color = '0.1')

ax.legend(fontsize = 15)
ax.set_xlabel('Distance (km)')
ax.set_ylabel('Velocity (m/s)')

savefig('figs/grassi_velocity_fitting.png', bbox_inches = 'tight')
savefig('figs/grassi_velocity_fitting.eps', bbox_inches = 'tight')
