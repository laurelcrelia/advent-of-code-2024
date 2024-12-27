def main(data, blinks):
    for stone in data.strip().split('\n'):
        stones = list(map(int, stone.split()))

    for i in range(blinks):
        stones = blink(stones)

    return len(stones)

def blink(stones):
    new_stones = []

    for stone in stones:

        # Rule 1: If the stone is 0, replace it with 1.
        if stone == 0:
            new_stones.append(1)

        # Rule 2: If the stone is an even number of digits, separate it into two stones. 
        elif len(str(stone)) % 2 == 0:
            num_str = str(stone)
            half_len = len(num_str) // 2
            first_half = num_str[:half_len].lstrip('0')
            second_half = num_str[half_len:].lstrip('0')
            # If the stripped half is empty, set it to "0"
            if not first_half:
                first_half = "0"
            if not second_half:
                second_half = "0"
            new_stones += [int(first_half), int(second_half)]

        # Rule 3: If none of the other rules apply, multiply it by 2024.
        else:
            prod = stone * 2024
            new_stones.append(prod)

    return new_stones


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        content = file.read()
    print(main(content, 25))