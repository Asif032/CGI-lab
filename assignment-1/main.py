import matplotlib.pyplot as plt

def draw_line(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    # Adjustments for m > 1
    is_steep = abs(dy) > abs(dx)
    if is_steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    swapped = False
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        swapped = True

    dx = x2 - x1
    dy = y2 - y1

    error = int(dx / 2.0)
    y_step = 1 if y1 < y2 else -1

    y = y1
    points = []

    for x in range(x1, x2 + 1):
        coord = (y, x) if is_steep else (x, y)
        points.append(coord)
        error -= abs(dy)
        if error < 0:
            y += y_step
            error += dx

    # If points were swapped, reverse the list
    if swapped:
        points.reverse()

    return points

# Case 1: (1,1), (8,4)
points_case1 = draw_line(1, 1, 8, 4)

# Case 2: (1,1), (4,8)
points_case2 = draw_line(1, 1, 4, 8)

# Visualization
def plot_line(points, case):
    x, y = zip(*points)
    plt.plot(x, y, label=f'Case {case}')

plot_line(points_case1, 1)
plot_line(points_case2, 2)

plt.scatter([1, 8, 4], [1, 4, 8], color='red')  # Marking endpoints
plt.title('Bresenham\'s Line Drawing Algorithm')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid(True)
plt.show()
