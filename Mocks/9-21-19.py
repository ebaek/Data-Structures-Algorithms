# Given two lists of strings as input, for example
# 	a: List[str] = ['hello', 'dad', 'orange', ...]
# 	b: List[str] = ['jeff', ...]
# write a function that determines if the intersection
# of these two lists is the empty set, i.e. there are no
# words in common

# find the list with the most words in it 
# iterate through all words of the list and check if the other list has the word

def intersectionIsEmptySet(a:List[str], b:List[str]) -> bool:
  shortest = set(a) if len(a) < len(b) else set(b)
  
# 	shortest = set()
#   longest = b
  
#   if len(a) > len(b):
#     longest = a
#     for idx in range(len(b)):
#       shortest.append(b[idx])
#   else:
#     for idx in range(len(a)):
#       shortest.append(a[idx])

  for idx in range(len(longest)):
    if longest[idx] in shortest: return False
  
  for word in longest:
    if word in shortest:
      return False
  
  return True
# Write a method to print out the powerset of an array
# Input: [1,2,3]
# Output: [[], [1], [2], [3], [1,2], [2,3], [1,3], [1,2,3]]

# base case is the length of the array is 0 so return empty array
# recursive step is:
	# remove element in the array and call powerset on the subarray
  # append subarray to the container array

def powerSet(arr: List[int]):
  ans = []
	if len(arr) == 0: return ans
  
  for idx in range(len(arr)):
    	ans.append(powerSet(arr[:idx] + arr[idx+1::]))
      # arr2 = copy(arr)
      # arr2.remove(idx)
      # powerSet(arr2)
  
  return ans.unique()

def powerSet(arr: List[int], arr2, index):
  if index >= len(arr):
    return []
  
  ans = []
  for idx in range(index, len(arr)):
      arr3 = copy(arr2)
      arr3.append(arr[idx])
      ans += powerSet(arr, arr3, index+1)
  
  return ans
      

# [1,2,3], [], 0
# powerSet([1,2,3], [1], 1)
	# powerSet([1,2,3], [1], 1)
	# powerSet([1,2,3], [1,2], 2)
# powerSet([1,2,3], [2], 2)
# powerSet([1,2,3], [3], 3)

# powerSet([2, 3])
# powerSet([3]) =>
# powerSet([]) => []

# powerSet([1, 3])
# powerSet([3]) => 
# powerSet([]) => []

# Given a magic function p(n) -- a primality test -- and a magic function
# l(n) which gives you the leftmost digit of any integer, write a method
# that will tell you if a non-zero integer n is a left-truncatable prime
# A left truncatable prime is a prime such that when the left digit is 
# truncated, the number is still a left-trundcatable prime. All single digit priems
# are left truncatable

# 335 -> l(n) -> 3 -> p(n) -> if false return False
# isLeftTruncatablePrime(35)
# retun True 

# base case is floor(divide by 10) = 0 and the number is prime return True
# recursive step: 
	# 

l(446) -> 46
l(46) -> 6
l(6) -> 0
  
def isLeftTruncatablePrime(n: int) -> bool:
  if not p(n): return False
	if l(n) == 0: return True
  return isLeftTruncatablePrime(l(n))
  
  
def isLeftTruncatablePrime(n: int) -> bool:
  if not p(n): return False
	if l(n) == 0: return True
  return isLeftTruncatablePrime(l(n))
  
  
# Follow up: now generate all left truncatable primes in the range [0, n]

def generateLeftTruncatablePrimes(n: int) -> List[int]:
	# insert code here
	pass

# --------------
# More Questions
# --------------

# Given a sorted array of integers, find the number of occurrences of each number
# Input: [1,1,1,1,1,1,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,4,4,4…]
# Output: {1: 7, 2: 3, 3: 10, 4: 3, … }

def numOccurrences(arr: List[int]) -> dict:
	# insert code here
	pass


# Given an array of intervals in the form of (i, j), where i,j are postive integers
# and i < j, write a method to coalesce 
# Input: [(0, 10), (5, 15), (6, 7), (20, 30)]
# Output: [(0, 15), (20, 30)]

def coalesceOverlappingWindows(arr: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
	# insert code here
	pass


# You are given an n by n square matrix. Show me how many unique ways 
# one can travel from point (0,0) to point (n,n) going only right and down

def uniquePaths(n: int) -> int:
	# insert code here
	pass


# Consider a binary matrix -- a 2-dimensional array of binary values
# Adjacent 1’s form an island. Delete all islands that touch the edge.

def deleteEdgeAdjacentIslands(arr: List[List[int]]):
	# insert code here
	pass


# Challenge
# https://www.hackerrank.com/challenges/reverse-shuffle-merge/problem