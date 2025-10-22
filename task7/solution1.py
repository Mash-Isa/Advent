if __name__ == "__main__":
    path = "task7/input"
    with open(path, "r") as f:
        lines = f.readlines()

    sum_true_answers = 0
    for line in lines:
        line = line.strip()
        answer = int(line.split(":")[0])
        numbers = list(map(int, line.split(":")[1].strip().split()))
        # find all combinfations of "*" and "+" possible with len(numbers) - 1 operators
        from itertools import product
        for ops in product(["+", "*"], repeat=len(numbers)-1):
            expr = ""
            for i, (n, op) in enumerate(zip(numbers, ops + ("",))):
                if i != 0:
                    n = f"{n})"
                expr += f"{n} {op} "
            expr = "(" * (len(numbers) - 1) + expr
            if eval(expr) == answer:
                sum_true_answers += answer
                break
    print(sum_true_answers)
