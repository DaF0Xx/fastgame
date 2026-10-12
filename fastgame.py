import random
import time
running = True

base = "A      |"
width = len(base)
print(len(base))
dist = width - 2
print("12345678")

while running:
    print(base, end="\r")

    if dist > 0:
        print("A" + " "*(dist-1) + "X", end="\r")
        dist -= 1
        time.sleep(0.5)

    else:
        dist = width - 2
