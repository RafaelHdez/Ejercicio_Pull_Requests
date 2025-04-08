import math
import time
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_galaxy(t):
    width, height = 80, 24
    cx, cy = width // 2, height // 2
    chars = ".,-~:;=!*#$@"
    galaxy = [[" " for _ in range(width)] for _ in range(height)]

    for i in range(100):
        angle = t + i * 0.3
        radius = i * 0.1
        x = int(cx + radius * math.cos(angle))
        y = int(cy + radius * math.sin(angle * 1.5))
        if 0 <= x < width and 0 <= y < height:
            galaxy[y][x] = chars[i % len(chars)]

    for row in galaxy:
        print("".join(row))

def run():
    t = 0
    try:
        while True:
            clear()
            draw_galaxy(t)
            t += 0.1
            time.sleep(0.05)
    except KeyboardInterrupt:
        print("\nAnimación terminada.")

if __name__ == "__main__":
    run()