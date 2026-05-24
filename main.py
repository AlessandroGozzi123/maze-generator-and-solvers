from collections import deque
import heapq
import time

def load_maze(path):
    grid = []
    start = goal = None
    with open(path, "r", encoding="utf-8") as f:
        for r, line in enumerate(f):
            line = line.rstrip("\n")
            if not line:
                continue
            row = list(line)
            for c, ch in enumerate(row):
                if ch == "S":
                    start = (r, c)
                elif ch == "G":
                    goal = (r, c)
            grid.append(row)
    if start is None or goal is None:
        raise ValueError("Mapa musí obsahovat S (start) a G (goal).")
    return grid, start, goal

def neighbors(grid, r, c):
    H, W = len(grid), len(grid[0])
    for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
        rr, cc = r + dr, c + dc
        if 0 <= rr < H and 0 <= cc < W and grid[rr][cc] != "#":
            yield (rr, cc)


def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def bfs(grid, start, goal):
    start_time = time.perf_counter()
    q = deque([start])
    parent = {start: None}
    expanded = 0

    while q:
        cur = q.popleft()
        expanded += 1

        if cur == goal:
            path = []
            while cur is not None:
                path.append(cur)
                cur = parent[cur]
            path.reverse()
            duration = (time.perf_counter() - start_time) * 1000
            return path, expanded, duration

        for nxt in neighbors(grid, cur[0], cur[1]):
            if nxt not in parent:
                parent[nxt] = cur
                q.append(nxt)

    return None, expanded, 0

def greedy_best_first(grid, start, goal):
    start_time = time.perf_counter()
    heap = [(manhattan(start, goal), start)]
    parent = {start: None}
    expanded = 0

    while heap:
        _, cur = heapq.heappop(heap)
        expanded += 1

        if cur == goal:
            path = []
            while cur:
                path.append(cur)
                cur = parent[cur]
            duration = (time.perf_counter() - start_time) * 1000
            return path[::-1], expanded, duration

        for nxt in neighbors(grid, *cur):
            if nxt not in parent:
                parent[nxt] = cur
                heapq.heappush(heap, (manhattan(nxt, goal), nxt))

    return None, expanded, 0

def a_star(grid, start, goal):
    start_time = time.perf_counter()
    heap = [(manhattan(start, goal), 0, start)]
    parent = {start: None}
    g_cost = {start: 0}
    expanded = 0

    while heap:
        _, g, cur = heapq.heappop(heap)
        expanded += 1

        if cur == goal:
            path = []
            while cur:
                path.append(cur)
                cur = parent[cur]
            duration = (time.perf_counter() - start_time) * 1000
            return path[::-1], expanded, duration

        for nxt in neighbors(grid, *cur):
            new_g = g + 1
            if nxt not in g_cost or new_g < g_cost[nxt]:
                g_cost[nxt] = new_g
                parent[nxt] = cur
                f = new_g + manhattan(nxt, goal)
                heapq.heappush(heap, (f, new_g, nxt))

    return None, expanded, 0



def draw_path(grid, path):
    out = [row[:] for row in grid]
    for (r, c) in path[1:-1]:
        if out[r][c] == ".":
            out[r][c] = "*"
    print("\n".join("".join(row) for row in out))

if __name__ == "__main__":

    input = input("Chcete vykreslit cestu v konzoli? (ano/ne): ").strip().lower()
    if input == "ano" or input == "a" or input == "y":
        draw_console = True
    else:
        draw_console = False

    grid, start, goal = load_maze("generated_maze.txt")
    path_bfs, exp_bfs, t_bfs = bfs(grid, start, goal)
    path_greedy, exp_greedy, t_greedy = greedy_best_first(grid, start, goal)
    path_astar, exp_astar, t_astar = a_star(grid, start, goal)


    print("=== BFS ===")
    if path_bfs:
        print(f"Délka cesty: {len(path_bfs)-1} kroků")
        print(f"Rozšířené uzly: {exp_bfs}")
        print(f"Čas hledání: {t_bfs:.4f} ms")
        
        if draw_console:
            draw_path(grid, path_bfs)
    else:
        print("Cesta nenalezena")

    print("\n=== Greedy Best-First Search ===")
    if path_greedy:
        print(f"Délka cesty: {len(path_greedy)-1} kroků")
        print(f"Rozšířené uzly: {exp_greedy}")
        print(f"Čas hledání: {t_greedy:.4f} ms")

        if draw_console:
            draw_path(grid, path_greedy)
    else:
        print("Cesta nenalezena")

    print("\n=== A* ===")
    if path_astar:
        print(f"Délka cesty: {len(path_astar)-1} kroků")
        print(f"Rozšířené uzly: {exp_astar}")
        print(f"Čas hledání: {t_astar:.4f} ms")
        
        if draw_console:
            draw_path(grid, path_astar)
    else:
        print("Cesta nenalezena")