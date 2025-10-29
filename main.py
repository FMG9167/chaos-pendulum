import matplotlib.pyplot as plt
import numpy as np
from math import cos, sin, pi, radians
from sympy import symbols, Eq, solve
import matplotlib.animation as animation

frames = 1000
m = 10
l = 10
L = 2 * l
dt=0.01

x1=[]
x2=[]
y1=[]
y2=[]
g = 98.1

o1=radians(105)
o2=radians(180)

def calc():
    w1=1
    w2=1


    global x1,x2,y1,y1,g,o1,o2,m1,m2,l,dt,frames

    j=-1
    while(j<frames):
        a1, a2 = symbols('x y')
        eq1 = Eq(a1 + 2*a2*(1+cos(o1-o2)),2*w2*(w1-w2)*sin(o1-o2))
        eq2 = Eq(2*w1*a1+w2*a2+(w1*a2+w2*a1)*cos(o1-o2),w1*w2*(w1-w2)*sin(o1-o2)+g*(1*w1*sin(o1) + w2*sin(o2)))
        dic = solve((eq1,eq2), (a1,a2))
        a1 = dic[a1]
        a2 = dic[a2]

        w1+=a1*dt
        w2+=a2*dt
        o1+=w1*dt
        o2+=w2*dt

        curx1 = l*sin(o1)
        curx2 = curx1 + l*sin(o2)
        cury1 = l*cos(o1)
        cury2 = cury1 + l*cos(o2)

        x1.append(curx1)
        x2.append(curx2)
        y1.append(cury1)
        y2.append(cury2)

        print(j)

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

# writer = animation.PillowWriter(fps=30,
#                                 metadata=dict(artist='Me'),
#                                 bitrate=1800)
# ani.save('chaos.gif', writer=writer)
plt.show()