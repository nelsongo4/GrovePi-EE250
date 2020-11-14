import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import datetime as dt
import time

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)


def animate(i):
    graph_data = open('/Users/Admin/PycharmProjects/pythonProject/examples.txt', 'r', encoding='utf-8-sig').read()
    lines = graph_data.split('\n')
    # print(lines)
    xs = []
    ys = []
    i = 0
    for line in lines:
        print(line)
        if len(line) > 0:
            y = line
            xs.append(i)
            # print(y)
            ys.append(float(y))
            print("DATA PROCESSING EXPECTS: ")
            print(sum(ys)/len(ys))
            i = i + 1
    ax1.clear()
    ax1.plot(xs, ys)

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
