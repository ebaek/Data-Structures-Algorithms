class Solution:
    def regionsBySlashes(self, grid):
        f = {}

        def find(x):
            f.setdefault(x, x)
            if x != f[x]:
                f[x] = find(f[x])
            return f[x]

        def union(x, y):
            f[find(x)] = find(y)

        for col in range(len(grid)):
            for row in range(len(grid)):
                if col:
                    union((col - 1, row, 2), (col, row, 0))
                if row:
                    union((col, row - 1, 1), (col, row, 3))
                if grid[col][row] != "/":
                    union((col, row, 0), (col, row, 1))
                    union((col, row, 2), (col, row, 3))
                if grid[col][row] != "\\":
                    union((col, row, 3), (col, row, 0))
                    union((col, row, 1), (col, row, 2))

        print(f)
        return len(set(map(find, f)))
