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
M1 = 10
M2 = 10
l1 = 1
l2 = 1
g = 9.81
o1=radians(90)
o2=radians(135)


L = l1+l2
x1=[]
y1=[]
x2=[]
y2=[]

def calc():
    w1=0
    w2=0
    global x1,y1,m1,M1,l1,o1,g,frames,dt,n,R
    global x2,y2,m2,M2,l2,o2

    j=-1
    while(j<frames):
        # a=-g * sin(o) / l - 6*pi*n*R*w/m
        K1 = -(m2*(w2**2)*l1*l2*sin(o1-o2)) - (g*l1*sin(o1)*((M1+M2)/2 + m1+m1))
        K2 = (m2*(w1**2)*l1*l2*sin(o1-o2)) - (g*l2*sin(o2)*((M2)/2 + m2))
        A1 = m1*(l1**2) + m2*(l2**2) + M1*(l1**2)/3
        B1 = m2*l1*l2*cos(o1-o2)
        A2 = m2*l1*l2*cos(o1-o2)
        B2 = m2*(l2**2) + M2*(l2**2)/3
        D = A1*B2 - A2*B1

        a1 = (B2*K1-B1*K2)/D
        a2 = (A1*K2-A2*K1)/D


        w1+=a1*dt
        o1+=w1*dt

        w2+=a2*dt
        o2+=w2*dt

        curx1=l1*sin(o1)
        cury1=-l1*cos(o1)

        curx2=curx1 + l2*sin(o2)
        cury2=cury1 - l2*cos(o2)


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
ani.save('double.gif', writer=writer)
# plt.show()