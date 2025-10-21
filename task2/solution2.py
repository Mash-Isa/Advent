import numpy as np

if __name__ == "__main__":
    path = "task2/input"
    with open(path, "r") as f:
        lines = f.readlines()
    
    reports = [np.array(line.strip().split()).astype(int) for line in lines]
    safe_reports_count = 0
    for report in reports:
        differences = np.abs(report[:-1] - report[1:])
        is_sorted = np.all(report == np.sort(report)) or np.all(report == np.sort(report)[::-1])
        if is_sorted and (differences >= 1).all() and (differences <= 3).all():
            safe_reports_count += 1
            continue
        # try removing each level
        for i in range(len(report)):
            new_report = np.delete(report, i)
            if len(new_report) < 2:
                continue
            new_differences = np.abs(new_report[:-1] - new_report[1:])
            new_sorted = np.all(new_report == np.sort(new_report)) or np.all(new_report == np.sort(new_report)[::-1])
            if new_sorted and (new_differences >= 1).all() and (new_differences <= 3).all():
                safe_reports_count += 1
                break

    print(safe_reports_count)