#1105: Filling Bookcase Shelves


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:

        def dfs(book_idx, shelf_height, shelf_remaining):

            if shelf_remaining < 0: return float('inf')
            if book_idx == len(books): return shelf_height

            book_width, book_height = books[book_idx]
            add_book = None
            next_shelf = None

            add_book = dfs(book_idx+1, max(book_height, shelf_height), shelf_remaining-book_width)
            memo[book_idx+1, max(book_height, shelf_height), shelf_remaining-book_width] = add_book

            next_shelf = shelf_height + dfs(book_idx+1, book_height, shelf_width-book_width)

            return min(add_book, next_shelf)

        return dfs(0, 0, shelf_width)


# Tabulation Approach
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        n = len(books)
        dp = [float('inf') for _ in range(n + 1)]
        dp[0] = 0
        for i in range(1, n + 1):
            max_width = shelf_width
            max_height = 0
            j = i - 1
            while j >= 0 and max_width - books[j][0] >= 0:
                max_width -= books[j][0]
                max_height = max(max_height, books[j][1])
                dp[i] = min(dp[i], dp[j] + max_height)
                j -= 1
        return dp[n]
