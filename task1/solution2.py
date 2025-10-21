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

    similarity_score = 0
    for num in list1:
        count = list2.count(num)
        score = num * count
        similarity_score += score
    print(similarity_score)