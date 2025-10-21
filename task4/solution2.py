import numpy as np

if __name__ == "__main__":
    path = "task4/input"
    with open(path, "r") as f:
        lines = f.readlines()

    grid = np.array([list(line.strip()) for line in lines])
    rows, cols = grid.shape
    count = 0

    for row in range(rows - 2):
        for col in range(cols - 2):
            center = grid[row + 1, col + 1]
            top_left = grid[row, col]
            top_right = grid[row, col + 2]
            bottom_left = grid[row + 2, col]
            bottom_right = grid[row + 2, col + 2]
            if center == "A":
                # S . S
                # . A .
                # M . M
                if top_left == "S" and top_right == "S" and bottom_left == "M" and bottom_right == "M":
                    count += 1
                # M . M
                # . A .
                # S . S
                if top_left == "M" and top_right == "M" and bottom_left == "S" and bottom_right == "S":
                    count += 1
                # M . S
                # . A .
                # M . S
                if top_left == "M" and top_right == "S" and bottom_left == "M" and bottom_right == "S":
                    count += 1
                # S . M
                # . A .
                # S . M
                if top_left == "S" and top_right == "M" and bottom_left == "S" and bottom_right == "M":
                    count += 1

    print(count)