def main(data):
    lines = data.strip().split('\n')

    word = "XMAS"
    counter = 0
    directions = [(0,1),(-1,0),(0,-1),(1,0),(1,1),(-1,-1),(-1,1),(1,-1)]
    grid = {}

    # create grid
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            char = lines[i][j]
            grid[(i,j)] = char

    # start from X
    for char in grid:
        if grid[char] == word[0]:

            # check all directions
            for dir in directions:
                pos = char
                for i in range(len(word)-1):
                    pos = (pos[0] + dir[0], pos[1] + dir[1])
                    if pos not in grid:
                        break
                    if i == 0 and grid[pos] != word[1]:
                        break
                    elif i == 1 and grid[pos] != word[2]:
                        break
                    elif i == 2 and grid[pos] == word[3]:
                        counter += 1

    return counter

if __name__ == "__main__":
    with open("input.txt", "r") as file:
        content = file.read()
    print(main(content))
