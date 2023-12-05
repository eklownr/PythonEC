import math


def calculate_distance(x1, y1, x2, y2):
    # Calculates the pythogorean distance between two objects
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def update_x(x1, x_vel, time_step):
    x2 = x1 + x_vel * time_step
    if x_vel > 0:
        x_vel2 -= x_vel * 0.1 * time_step
    return x2, x_vel2
