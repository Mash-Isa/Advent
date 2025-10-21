if __name__ == "__main__":
    path = "task1/input"
    with open(path, "r") as f:
        lines = f.readlines()
    
    list1 = []
    list2 = []
    for line in lines:
        nums = line.strip().split()
        if len(nums) >= 2:
            list1.append(int(nums[0]))
            list2.append(int(nums[1]))

    list1.sort()
    list2.sort()

    distances = [abs(a - b) for a, b in zip(list1, list2)]

    print(sum(distances))