#!/usr/bin/python3

import re

import matplotlib.pyplot as plt
import numpy as np

with open("measure.log", "r") as f:
    content = f.readlines()


NUM_THREADS = 16
pattern = r"\d\.\d\d"


view1 = []
view2 = []


def find_speedup(s: str) -> float:
    match = re.findall(pattern, s)
    return float(match[0])


for i in range(NUM_THREADS - 1):
    view1str = content[5 + 11 * i]
    view2str = content[10 + 11 * i]

    view1speedup = find_speedup(view1str)
    view1.append(view1speedup)
    view2speedup = find_speedup(view2str)
    view2.append(view2speedup)


x = list(range(2, NUM_THREADS + 1))

plt.plot(x, view1, label="view 1")
plt.plot(x, view2, label="view 2")
plt.xticks(np.arange(2, NUM_THREADS + 1, 1))

# naming the x axis
plt.xlabel("Number of threads")

# naming the y axis
plt.ylabel("Speedup")

# giving a title to my graph
plt.title("Mandelbrot speedup")

plt.legend()

# function to show the plot
plt.savefig("measure.png")
plt.show()
