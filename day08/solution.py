def main(data):
    matrix = [list(line) for line in data.splitlines()]
    antennas = [list(line) for line in data.splitlines()]
    characters = {}

    # Find all the distinct antennas as keys and arrange all antenna coordinates as values
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if matrix[x][y] != ".":
                if matrix[x][y] in characters:
                    characters[matrix[x][y]].append((x, y))
                else:
                    characters[matrix[x][y]] = [(x, y)]

    # Find the pairs of antennas that are within right distance
    for y in characters:
        for i, pos1 in enumerate(characters[y]):
            for j, pos2 in enumerate(characters[y]):
                if i < j:
                    if abs(pos1[0] - pos2[0])*abs(pos1[1] - pos2[1])!=0: 
                        antennas = create_antinodes(pos1, pos2, antennas)

    # Find the number of antinodes
    antinodes = 0
    for x in antennas:
        antinodes += x.count("#")

    return antinodes

# Add the antinodes for the two given antennas
def create_antinodes(char1, char2, matrix):
    difference = ((char2[0] - char1[0]),(char2[1] - char1[1]))
    antinode1 = (char1[0]-difference[0], char1[1]-difference[1])
    antinode2 = (char2[0]+difference[0], char2[1]+difference[1])

    # Put antinodes to the antenna matrix if their coordinates are within the matrix range
    if (antinode1[0] >= 0 and antinode1[0] < len(matrix)) and (antinode1[1] >= 0 and  antinode1[1] < len(matrix)):
        matrix[antinode1[0]][antinode1[1]] = "#"
    if (antinode2[0] >= 0 and antinode2[0] < len(matrix)) and (antinode2[1] >= 0 and  antinode2[1] < len(matrix)):
        matrix[antinode2[0]][antinode2[1]] = "#"
    
    return matrix


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        content = file.read()
    print(main(content))
