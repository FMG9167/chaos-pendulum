import matplotlib.pyplot as plt
import numpy as np
from math import cos, sin, pi, radians, atan
from sympy import symbols, Eq, solve
import matplotlib.animation as animation

frames = 5000
m = 10
l = 1
L = 2 * l
dt=0.01

x=[]
y=[]
g = 9.81

o=radians(60)

def calc():
    w=0
    global x,y,m,g,o,frames,dt,l

    j=-1
    while(j<frames):
        a=-g * sin(o) / l
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

# writer = animation.PillowWriter(fps=30,
#                                 metadata=dict(artist='Me'),
#                                 bitrate=1800)
# ani.save('chaos.gif', writer=writer)
plt.show()