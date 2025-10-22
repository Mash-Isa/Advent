def custom_eval(numbers, ops):
    expr = [(n, op) for n, op in zip(numbers, ops + ("",))]
    i = 0
    while i < len(expr) - 1:
        n, op = expr[i]
        next_n, next_op = expr[i + 1]
        if op == "||":
            # concatenate n and next_n
            new_n = int(str(n) + str(next_n))
            # replace in expr
            expr[i] = (new_n, next_op)
            del expr[i + 1]
            i = max(i - 1, 0)  # step back to catch consecutive ||
        else:
            i += 1
    # evaluate left to right
    result = expr[0][0]
    for i in range(len(expr)-1):
        op = expr[i][1]
        next_n = expr[i+1][0]
        if op == "+":
            result += next_n
        elif op == "*":
            result *= next_n
    return result


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
        for ops in product(["+", "*", "||"], repeat=len(numbers)-1):
            if custom_eval(numbers, ops) == answer:
                sum_true_answers += answer
                break

    print(sum_true_answers)
