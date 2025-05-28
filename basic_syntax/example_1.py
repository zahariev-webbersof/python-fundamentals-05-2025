import math

def heart_pattern():
    for y in range(20, -20, -1):
        line = ''
        for x in range(-30, 30):
            if (((x * 0.04) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (x * 0.04) ** 2 * (y * 0.1) ** 3) <= 0:
                line += '*'
            else:
                line += ' '
        print(line)

heart_pattern()