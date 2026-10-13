import random
import time
running = True

screen = "A              |"
base = screen
width = len(screen)
pos = [0, width - 3, 0, width]
print(len(screen))
print("1234567890123456")

while running:
    print(screen, end="\r")

    if pos[1] >= 0:
        if pos[1] <= 3:
            screen = "A" + " "*pos[1] + "X" + " "*(pos[2]-1) + "X"
            pos[1] -= 1
        else:
            screen = "A" + " "*pos[1] + "X"
            pos[1] -= 1
            pos[2] += 1
        time.sleep(0.5)

    else:
        pos[1] = pos[2]-1
        pos[2] = width - pos[2] - 2

    print(base, end="\r")
    