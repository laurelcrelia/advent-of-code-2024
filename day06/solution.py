def main(data):

    matrix = [list(line) for line in data.splitlines()]
    directions = {
    "^": (-1, 0),
    "v": (1, 0),
    ">": (0, 1),
    "<": (0, -1)
    }
    current = "^"

    # find the starting position
    found = False
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if matrix[x][y] == "^":
                found = True
                break
        if found:
            break

    ready = False
    while not ready:

        if x == 0 or x == len(matrix)-1 or y == 0 or y == len(matrix[0])-1:
            matrix[x][y] = "X"
            ready = True
            break

        (new_x, new_y) = x + directions[current][0], y + directions[current][1]

        if matrix[new_x][new_y] == "#":
            if matrix[x][y] == "^":
                matrix[x][y] = ">"
            elif matrix[x][y] == ">":
                matrix[x][y] = "v"
            elif matrix[x][y] == "v":
                matrix[x][y] = "<"
            elif matrix[x][y] == "<":
                matrix[x][y] = "^"
            current = matrix[x][y]

        elif matrix[new_x][new_y] == ".":
            matrix[x][y] = "X"
            matrix[new_x][new_y] = current
            (x, y) = (new_x, new_y)

        elif matrix[new_x][new_y] == "X":
            matrix[x][y] = "X"
            matrix[new_x][new_y] = current
            (x, y) = (new_x, new_y)

    return count_steps(matrix)

def count_steps(matrix):
    counter = 0
    for row in matrix:
        for element in row:
            if element == "X":
                counter += 1
    return counter

if __name__ == "__main__":
    with open("input.txt", "r") as file:
        content = file.read()
    print(main(content))
