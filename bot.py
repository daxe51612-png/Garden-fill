ROWS = 10
COLS= 9
START= (0,1)
DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
  def solve(grid):
    path = [START]
    visited = {START}

    def dfs(r, c):
        if len(path) == sum(row.count(0) for row in grid):
            return True

        for dr, dc in DIRECTIONS:
            nr, nc = r + dr, c + dc

            if not (0 <= nr < ROWS and 0 <= nc < COLS):
                continue
            if grid[nr][nc] != 0:
                continue
            if (nr, nc) in visited:
                continue

            visited.add((nr, nc))
            path.append((nr, nc))

            if dfs(nr, nc):
                return True

            path.pop()
            visited.remove((nr, nc))

        return False

    if dfs(*START):
        return path

    return None
