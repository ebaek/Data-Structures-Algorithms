# 733: Flood Fill

# DFS Approach
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        rows, cols, orig_color = len(image), len(image[0]), image[sr][sc]
        
        def traverse(row, col):
            if(not (0 <= row < rows and 0 <= col < cols) or image[row][col] != orig_color):
                return
            
            image[row][col] = newColor
            
            [traverse(row + x, col + y) for (x, y) in ((0, 1), (1, 0), (-1, 0), (0, -1))]
        
        if orig_color != newColor: traverse(sr, sc)
            
        return image
    
# BFS Approach
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        orig_color, row, col = image[sr][sc], len(image), len(image[0])
        if orig_color != newColor:
            q = collections.deque([(sr, sc)])
            while q:
                i, j = q.popleft()
                image[i][j] = newColor
                for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= x < row and 0 <= y < col and image[x][y] == orig_color:
                        q.append((x, y))
        return image
            
            
            

        
        
            
