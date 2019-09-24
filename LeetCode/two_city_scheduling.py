# 1029: Two City Scheduling

# There are 2N people a company is planning to interview. 
# The cost of flying the i-th person to city A is costs[i][0], 
# and the cost of flying the i-th person to city B is costs[i][1].

# Return the minimum cost to fly every person to a city such that 
# exactly N people arrive in each city.

# Input: [
    # [10,20],
    # [30,200],
    # [400,50],
    # [30,20]]

# Output: 110
# Explanation: 
# The first person goes to city A for a cost of 10.
# The second person goes to city A for a cost of 30.
# The third person goes to city B for a cost of 50.
# The fourth person goes to city B for a cost of 20.

# The total minimum cost is 10 + 30 + 50 + 20 = 110 to 
# have half the people interviewing in each city.

# Approach: 
# sort by the difference in the cost of a v.s. b 
# send person a to first half of sorted trips, and send b to the second half of sorted trips

# Example:

# Input: [
    # [10,20], -> -10
    # [30,200],  -> -170
    # [400,50],  -> 350
    # [30,20]]   -> 10

# Sorted: [
    # [30,200],  -> -170
    # [10,20], -> -10
    # [30,20]]   -> 10
    # [400,50],  -> 350

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs = sorted(costs, key=lambda x: x[0] - x[1])
                    
        aTrips = len(costs) // 2
        totalCost = 0

        for trip in range(aTrips):
            totalCost += costs[trip][0]
            totalCost += costs[trip + aTrips][1]

        return totalCost




