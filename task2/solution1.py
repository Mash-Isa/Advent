import numpy as np

if __name__ == "__main__":
    path = "task2/input"
    with open(path, "r") as f:
        lines = f.readlines()
    
    reports = [np.array(line.strip().split()).astype(int) for line in lines]
    safe_reports_count = 0
    for report in reports:
        if ((report == np.sort(report)[::-1]).all()) or ((report == np.sort(report)).all()):
            differences = np.abs(report[:-1] - report[1:])
            if (not (differences < 1).any()) and (not (differences > 3).any()):
                safe_reports_count += 1
    print(safe_reports_count)