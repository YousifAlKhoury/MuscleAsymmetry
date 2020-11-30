import numpy as np
import matplotlib as mpl
mpl.use("TkAgg")
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
from read import text
import read
import tkinter as tk
# from walking import update_lines as update_lines1
# from anklePlot import update_lines as update_lines2
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import messagebox

from tkinter import font as tkFont

HEIGHT = 1000
WIDTH = 1000

RightSS = read.readRightSS("frame.txt")
LeftSS = read.readLeftSS("frame.txt")

colors = ['r', 'g']
width =  [-0.5, 0.5] 
ratioL = -width[0] *100
ratioR = width[1] *100
textleft = []
textright = []

start = 1

#########################################################

def ExitApplication():
    MsgBox = tk.messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
    if MsgBox == 'yes':
       root.destroy()
    else:
        tk.messagebox.showinfo('Return','You will now return to the application screen')

#########################################################

def StartApplication():
    global start
    start = not start

    if start:
        line_ani1.event_source.start()
        line_ani2.event_source.start()
        line_ani3.event_source.start()
    else:
        line_ani1.event_source.stop()
        line_ani2.event_source.stop()
        line_ani3.event_source.stop()

#########################################################

def update_lines2(num):
    global start
    lines[0].set_data(range(num), ankleRightData[:num])
    lines[1].set_data(range(num), ankleLeftData[:num])

    return lines

#########################################################

def update_lines1(num, lines):
    global start
    data = read.retrieveCoordinates(text[num])
    frame = read.retrieveFrame(data)
    ax.clear()

    ax.set_title('Movement')

    ax.set_xlim([-1, 1])
    ax.set_ylim([-3.2, 1])
    ax.set_zlim([-1, 1]) 

    ax.set_xlabel('X')

    ax.set_ylabel('Y')

    ax.set_zlabel('Vertical')

    data = read.retrieveCoordinates(text[num])

    frame = read.retrieveFrame(data)

    lines = [ax.plot(line[0], line[1], line[2])[0] for line in frame]

    return lines

#########################################################

def update_lines3(i):
    global width, ratioL, ratioR, textleft, textright, start
    for bar in ax3.containers:
        bar.remove()
    
    textleft.set_visible(False)
    textright.set_visible(False)

    y = 0

    if(i == 0):
        width =  [-0.5, 0.5] 
        ratioL = -width[0] *100
        ratioR = width[1] *100

    if (i==RightSS[0][1]):
        left = -(LeftSS[2]/(LeftSS[2]+RightSS[0][2]))
        right = 1+left
        
        width = [left, right]

        ratioL = -left *100
        ratioR = right *100
    elif(i==RightSS[1][1]):
        left = -(LeftSS[2]/(LeftSS[2]+RightSS[1][2]))
        right = 1+left
        
        width = [left, right]

        ratioL = -left *100
        ratioR = right *100
    
    ax3.barh(y=y, height = 0.4, width=width, color=colors)
    textleft = plt.text(-0.4, 0.25, str(round(ratioL, 2))+'%', horizontalalignment='center', fontsize = 14)
    textright = plt.text(0.4, 0.25, str(round(ratioR, 2))+'%', horizontalalignment='center', fontsize = 14)

    return ax3

#########################################################

fig = plt.figure(1, figsize=(8, 8))

ax = fig.gca(projection='3d')
ax.set_title('Movement')

ax.set_xlim([-1, 1])
ax.set_ylim([-3.2, 1])
ax.set_zlim([-1, 1]) 

ax.set_xlabel('X')

ax.set_ylabel('Y')

ax.set_zlabel('Vertical')

data = read.retrieveCoordinates(text[0])

frame = read.retrieveFrame(data)

lines = [ax.plot(line[0], line[1], line[2])[0] for line in frame]   

#########################################################

ankleLeftData = read.getVerticalAnkleLeft(text)
ankleRightData = read.getVerticalAnkleRight(text)

minVal = min(min(ankleLeftData), min(ankleRightData))
maxVal = max(max(ankleLeftData), max(ankleRightData))

#########################################################

fig1 = plt.figure(2, figsize=(9,4))
ax1 = fig1.add_subplot()
line1 = ax1.plot([], [], 'r-', label="Right ankle")[0]
line2 = ax1.plot([], [], 'g-', label="Left ankle")[0]

lines = []
lines.append(line1)
lines.append(line2)

plt.xlim(0, len(text))
plt.ylim(minVal, maxVal)

plt.xlabel('Time (frame)')
plt.ylabel('Position')

plt.title('Vertical Position of Ankle')

plt.legend()

#########################################################

fig3 = plt.figure(3, figsize=(9,2))
ax3 = fig3.add_subplot()
ax3.barh(width=width, y=0, height = 0.4, color = colors)
plt.xlim(-1, 1)
plt.ylim(-0.5, 0.5)
plt.axis('off')

plt.title('Asymmetry Index')

textleft = plt.text(-0.4, 0.25, str(round(ratioL, 2))+'%', horizontalalignment='center', fontsize = 14)
textright = plt.text(0.4, 0.25, str(round(ratioR, 2))+'%', horizontalalignment='center', fontsize = 14)

#########################################################

root = tk.Tk()

myFont = tkFont.Font(family='Helvetica', size = 18)
root.attributes('-fullscreen', True)
root.configure(bg='#FFFFFF')

f = tk.Frame(root)

#########################################################

button1 = tk.Button (f, text='Exit Application',command=ExitApplication,bg='brown',fg='#FFFFFF', height = 2, width = 15, font=myFont)
button1.grid(row = 1, column = 0, padx=5, pady=5)

#########################################################

button = tk.Button(f, text='Start / Pause Model',command=StartApplication,bg='brown',fg='#FFFFFF', height = 2, width = 15, font=myFont)
button.grid(row = 0, column = 0, padx=5, pady=5)

f.grid(row = 1, column = 0)
#########################################################

canvas0 = FigureCanvasTkAgg(fig, master=root)
canvas0.get_tk_widget().grid(row = 0, column = 0)

############################################

canvas1 = FigureCanvasTkAgg(fig1, master=root)
canvas1.get_tk_widget().grid(row = 0, column = 1)

#########################################################

canvas2 = FigureCanvasTkAgg(fig3, master=root)
canvas2.get_tk_widget().grid(row = 1, column = 1)

#########################################################

line_ani1 = animation.FuncAnimation(fig, update_lines1, frames=np.arange(1,len(text)-1), fargs=(lines, ),
                                   interval=5, blit=False)
line_ani2 = animation.FuncAnimation(fig1, update_lines2, frames=np.arange(0,len(text)-1),
                                   interval=5, blit=False)
line_ani3 = animation.FuncAnimation(fig3, func=update_lines3, frames=np.arange(0,len(text)-1),
                     interval=5, blit=False)

#########################################################

tk.mainloop()