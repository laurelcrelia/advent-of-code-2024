def main(content):
    data = parse_data(content)
    count = 0
    for i in range(len(data)):
        if is_safe(data[i]):
            count += 1
    return count

def parse_data(data):
    lines = data.strip().split('\n')
    result = []
    for line in lines:
        result.append(list(map(int, line.split())))
    return result

def is_safe(report):
    if report[0] < report[-1]:
        return increases(report)
    elif report[0] > report[-1]:
        return decreases(report)
    else:
        return False

def increases(report):
    for i in range(len(report) - 1):
        if report[i + 1] - report[i] not in [1, 2, 3]:
            return False
    return True

def decreases(report):
    for i in range(len(report) - 1):
        if report[i] - report[i + 1] not in [1, 2, 3]:
            return False
    return True

if __name__ == "__main__":
    with open('input.txt', 'r') as file:
        content = file.read()
    print(main(content))