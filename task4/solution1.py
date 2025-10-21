import numpy as np

if __name__ == "__main__":
    path = "task4/input"
    with open(path, "r") as f:
        lines = f.readlines()

    word = "XMAS"
    word_len = len(word)
    directions = [
        (0, 1),    # right
        (0, -1),   # left
        (1, 0),    # down
        (-1, 0),   # up
        (1, 1),    # down-right
        (1, -1),   # down-left
        (-1, 1),   # up-right
        (-1, -1),  # up-left
    ]

    grid = np.array([list(line.strip()) for line in lines])
    rows, cols = grid.shape
    total_count = 0

    for row in range(rows):
        for col in range(cols):
            for row_step, col_step in directions:
                indices_row = row + np.arange(word_len) * row_step
                indices_col = col + np.arange(word_len) * col_step
                if np.all((0 <= indices_row) & (indices_row < rows) & (0 <= indices_col) & (indices_col < cols)):
                    chars = grid[indices_row, indices_col]
                    if np.array_equal(chars, np.array(list(word))):
                        total_count += 1

    print(total_count)