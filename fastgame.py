import random
import time
running = True

base = "A              |"
width = len(base)
print(len(base))
dist = width - 3
dist2 = 0
print("1234567890123456")

while running:
    print(base, end="\r")

    if dist >= 0:
        if dist <= 3:
            print("A" + " "*dist + "X" + " "*(dist2-1) + "X", end="\r")
            dist -= 1
            time.sleep(0.5)

        else:
            print("A" + " "*dist + "X", end="\r")
            dist -= 1
            dist2 += 1
            time.sleep(0.5)

    else:
        dist = width - 3
        dist2 = 0

    

