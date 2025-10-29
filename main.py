import matplotlib.pyplot as plt
import numpy as np
from math import cos, sin, pi, radians, atan, floor
from sympy import symbols, Eq, solve
import matplotlib.animation as animation

dt=0.03
t=20
frames = int(t//dt)
m1 = 10
m2 = 10
l = 1
L = 2 * l
x1=[]
y1=[]
x2=[]
y2=[]
g = 9.81
n=0.1
R=1

o1=radians(90)
o2=radians(135)

def calc():
    w1=0
    w2=0
    global x1,y1,m1,o1,g,frames,dt,l,n,R
    global x2,y2,m2,o2

    j=-1
    while(j<frames):
        # a=-g * sin(o) / l - 6*pi*n*R*w/m
        a1=-g * sin(o1) / l
        w1+=a1*dt
        o1+=w1*dt

        a2=-g * sin(o2) / l
        w2+=a2*dt
        o2+=w2*dt

        curx1=l*sin(o1)
        cury1=-l*cos(o1)

        curx2=curx1 + l*sin(o2)
        cury2=cury1 - l*cos(o2)


        x1.append(curx1)
        y1.append(cury1)

        x2.append(curx2)
        y2.append(cury2)

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
    thisx = [0, x1[i], x2[i]]
    thisy = [0, y1[i], y2[i]]

    history_x = x2[:i]
    history_y = y2[:i]

    line.set_data(thisx, thisy)
    trace.set_data(history_x, history_y)
    time_text.set_text(time_template % (i*dt))
    return line, trace, time_text


ani = animation.FuncAnimation(
    fig, animate, frames, interval=dt*1000, blit=True)

writer = animation.PillowWriter(fps=30,bitrate=1800)
ani.save('doublesimple.gif', writer=writer)
# plt.show()