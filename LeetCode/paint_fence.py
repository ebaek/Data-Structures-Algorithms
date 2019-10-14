# Paint Fence: 276 

# simply add these for your answer:
# num_ways(i) = num_ways_diff(i) + num_ways_same(i)

# num_ways_diff(i) = num_ways(i-1) * (k-1)
# num_ways_same(i) = num_ways_diff(i-1) * 1

# num_ways(i) = num_ways_diff(i) + num_ways_same(i)
# = num_ways(i-1) * (k-1) + num_ways_diff(i-1)

# We know how to compute num_ways_diff, so we can substitute:
# num_ways(i) = num_ways(i-1) * (k-1) + num_ways(i-2) * (k-1)

# num_ways(i) = (num_ways(i-1) + num_ways(i-2)) * (k-1)

class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 0: return 0
        if n == 1: return k
        if n == 2: return k*k

        table = [0 for _ in range(n+1)]
        table[0] = 0
        table[1] = k
        table[2] = k*k

        for i in range(3, n+1):
            table[i] = (table[i-1] + table[i-2]) * (k-1)

        return table[n]
