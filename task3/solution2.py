import re

if __name__ == "__main__":
    path = "task3/input"
    with open(path, "r") as f:
        lines = f.readlines()
    positions = {}

    for line_idx, line in enumerate(lines):
        for m in re.finditer(r"do\(\)", line):
            positions[(line_idx, m.start())] = True
        for m in re.finditer(r"don't\(\)", line):
            positions[(line_idx, m.start())] = False
        for m in re.finditer(r"mul\((\d+),(\d+)\)", line):
            positions[(line_idx, m.start())] = (int(m.group(1)), int(m.group(2)))

    sorted_positions = sorted(positions.items())

    enabled = True
    total_sum_multiplications = 0
    for pos, val in sorted_positions:
        if isinstance(val, bool):
            enabled = val
        elif isinstance(val, tuple):
            if enabled:
                total_sum_multiplications += val[0] * val[1]

    print(total_sum_multiplications)