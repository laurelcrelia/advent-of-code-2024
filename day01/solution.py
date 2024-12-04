def parse_data(data):
    lines = data.strip().split('\n')
    left_values = []
    right_values = []
    for line in lines:
        left, right = map(int, line.split())
        left_values.append(left)
        right_values.append(right)
    return left_values, right_values

def total_distance(s):
    parsed_data = parse_data(s)
    left_list = parsed_data[0]
    right_list = parsed_data[1]
    count = 0
    lenght = len(left_list) 
    i = 0
    while i < lenght:
        min_left = min(left_list)
        min_right = min(right_list)
        count += abs(min_left - min_right)
        right_list.pop((right_list.index(min_right)))
        left_list.pop((left_list.index(min_left)))
        i += 1

    return count

if __name__ == "__main__":
    with open('input.txt', 'r') as file:
        content = file.read()
    print(total_distance(content))