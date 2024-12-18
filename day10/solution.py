def main(data):
    grid = [list(line) for line in data.splitlines()]

    sum = 0

    for i in range(len(grid)):
        for j in range(len(grid)):
            sum += trailhead_sum(grid, i, j)

    return sum

def within_bounds(lenght, i, j):
    return 0 <= i < lenght and 0 <= j < lenght

def trailhead_sum(grid, i, j):

    if grid[i][j] != "0":
        return 0

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    trailhead_sum = 0
    visited = ([[False for i in range(len(grid))]for j in range(len(grid))])
    stack = [(i, j)]

    while len(stack) > 0:
        current_i, current_j = stack.pop()
        current = int(grid[current_i][current_j])

        if visited[current_i][current_j]:
             continue
        visited[current_i][current_j] = True

        if current == 9:
            trailhead_sum += 1
            continue

        for di, dj in directions:
            if not within_bounds(len(grid), current_i+di, current_j+dj):
                continue
            
            next = int(grid[current_i+di][current_j+dj])
            if next != current + 1:
                continue
            stack.append((current_i+di, current_j+dj))
            
    return trailhead_sum


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        content = file.read()
    print(main(content))
