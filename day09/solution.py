def main(data):

    # Parse the input into a list of integers e.g. "12345"->[1, 2, 3, 4, 5]
    disk_map = [int(x) for x in data.strip()]

    # First rearrangement of the disk to result in "0..111....22222" pattern
    phase1 = []
    id = -1
    for i in range(0,len(disk_map)):
        if i % 2 == 0:
            id += 1
            for j in range(disk_map[i]):
                phase1.append(id)
        else:   
            for j in range(disk_map[i]):
                phase1.append(".")

    # Second rearrangement of the disk to result in "022111222......" pattern
    left_pointer = 0
    right_pointer = len(phase1) - 1
    while left_pointer < right_pointer:
        # iterate through the left pointer until it finds a "."
        while left_pointer < len(phase1) and phase1[left_pointer] != ".":
            left_pointer += 1

        # iterate through the right pointer until it finds an integer
        while right_pointer >= 0 and phase1[right_pointer] == ".":
            right_pointer -= 1

        if left_pointer < right_pointer:
            # swap the elements
            phase1[left_pointer], phase1[right_pointer] = phase1[right_pointer], phase1[left_pointer]
            left_pointer += 1
            right_pointer -= 1

    # Checksum calculation
    sum = 0
    for i in range(0, len(phase1)):
        if phase1[i] == ".":
            break
        sum += phase1[i]*i

    return sum

if __name__ == "__main__":
    with open("input.txt", "r") as file:
        content = file.read()
    print(main(content))
