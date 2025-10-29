import matplotlib.pyplot as plt
import numpy as np
from math import cos, sin, pi, radians, atan, floor
from sympy import symbols, Eq, solve
import matplotlib.animation as animation

dt=0.03
t=10
frames = int(t//dt)
m = 10
l = 1
L = 2 * l
x=[]
y=[]
g = 9.81
n=0.1
R=1

o=radians(60)

def calc():
    w=0
    global x,y,m,g,o,frames,dt,l,n,R

    j=-1
    while(j<frames):
        a=-g * sin(o) / l - 6*pi*n*R*w/m
        w+=a*dt
        o+=w*dt

        curx=l*sin(o)
        cury=-l*cos(o)
        
        x.append(curx)
        y.append(cury)

        j+=1
calc()

fig = plt.figure(figsize=(5, 4))
ax = fig.add_subplot(autoscale_on=False, xlim=(-L, L), ylim=(-L, L))
ax.set_aspect('equal')
ax.grid()

line, = ax.plot([], [], 'o-', lw=2)
trace, = ax.plot([], [], '.-', lw=1, ms=2)
time_template = 'time = %.1fs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)


def animate(i):
    thisx = [0, x[i]]
    thisy = [0, y[i]]

    history_x = x[:i]
    history_y = y[:i]

    line.set_data(thisx, thisy)
    trace.set_data(history_x, history_y)
    time_text.set_text(time_template % (i*dt))
    return line, trace, time_text


ani = animation.FuncAnimation(
    fig, animate, frames, interval=dt*1000, blit=True)

writer = animation.PillowWriter(fps=30,bitrate=1800)
ani.save('drag.gif', writer=writer)
# plt.show()