from itertools import product

def main(data):
    result = 0

    for line in data.strip().split('\n'):
        target, numbers = line.split(': ')
        target = int(target)
        numbers = list(map(int, numbers.split()))
        
        for combination in product("*+", repeat=len(numbers)-1):
            total = numbers[0]
            for i in range(len(combination)):
                if combination[i] == '+':
                    total += numbers[i+1]
                if combination[i] == '*':
                    total *= numbers[i+1]
            if total == target:
                result += target
                break

    return result

if __name__ == "__main__":
    with open("input.txt", "r") as file:
        content = file.read()
    print(main(content))
