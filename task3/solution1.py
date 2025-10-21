import re

if __name__ == "__main__":
    path = "task3/input"
    with open(path, "r") as f:
        lines = f.readlines()
    total_sum_multiplications = 0
    for line in lines: 
        # look for structure like mul(number,number) and extract the two numbers
        matches = re.findall(r'mul\((\d+),(\d+)\)', line)
        sum_multiplications = sum(int(a) * int(b) for a, b in matches)
        total_sum_multiplications += sum_multiplications
    print(total_sum_multiplications)