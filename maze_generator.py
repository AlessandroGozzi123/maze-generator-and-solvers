import random
import sys

def generate_maze():

    sys.setrecursionlimit(5000)

    try:
        size = int(input("Zadejte velikost bludiště: "))
    except ValueError:
        print("Je potřeba zadat číslo. Zkuste to znovu.")
        return

    if size % 2 == 0:
        size += 1
    
    width = size
    height = size

    grid = [["#" for _ in range(width)] for _ in range(height)]

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def carve_passages_from(cx, cy):
        
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = cx + (dx * 2), cy + (dy * 2)

            if 0 <= nx < width and 0 <= ny < height and grid[ny][nx] == "#":
                grid[ny][nx] = "."
                grid[cy + dy][cx + dx] = "."
                
                carve_passages_from(nx, ny)

    grid[1][1] = "."
    carve_passages_from(1, 1)

    grid[1][1] = "S"
    grid[height - 2][width - 2] = "G"

    filename = "generated_maze.txt"
    with open(filename, "w") as f:
        for row in grid:
            f.write("".join(row) + "\n")

    print(f"Hotovo. Bludiště o velikosti {width}x{height} bylo uloženo do {filename}")

if __name__ == "__main__":
    generate_maze()