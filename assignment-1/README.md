# Bresenham's Line Drawing Algorithm

This Python script implements Bresenham's Line Drawing Algorithm to draw lines with slopes 0 < m < 1 and m > 1. The implementation is based on the provided inputs for two cases:

## Inputs
1. Case 1: (1,1), (8,4)
2. Case 2: (1,1), (4,8)

## Functions
1. The `draw_line` function calculates the points on the line using Bresenham's algorithm. It handles cases where the slope (m) is between 0 and 1 and when m is greater than 1. Adjustments are made to the algorithm based on whether the line is steep or not.
2. The `plot_line` function uses matplotlib to plot the line segments and scatter points for visualization.

## Adjustments for m > 1
The algorithm is adjusted to handle slopes greater than 1. The adjustments include swapping x and y coordinates when the slope is steep (abs(dy) > abs(dx)) and reversing the order of points if necessary.

## Visualization
The script uses the `matplotlib` library to visualize the line segments and scatter points for the given cases. The points are marked in red, representing the endpoints of the lines.

## How to Run
1. Ensure you have Python installed.
2. Install the required library:
   ```bash
   pip install matplotlib
