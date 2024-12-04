import re

def main(content):
    data = parse_data(content)
    counter = 0
    for sequence in data:
        result = multiplyer(sequence)
        counter += result
    return counter

# parse all correct sequences to list and then separate only integers and save them as tuples
def parse_data(data):
    sequences = re.findall(r"mul\(\d{1,3},\d{1,3}\)", data)
    result = []
    for seq in sequences:
        numbers = re.findall(r"\d+", seq)
        result.append((int(numbers[0]), int(numbers[1])))
    return result

# multiply the tuples that were already parsed to integers
def multiplyer(sequence):
    multiplied = sequence[0] * sequence[1]
    return multiplied

if __name__ == "__main__":
    with open("input.txt", "r") as file:
        content = file.read()
    print(main(content))