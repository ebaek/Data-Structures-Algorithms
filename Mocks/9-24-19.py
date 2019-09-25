# 9/24/19

# Given a string, reduce the string by removing 3 or more consecutive identical characters. 
# You should greedily remove characters from left to right.

# Input: "aaabbbc"
# Output: "c"
# Explanation:
# 1. Remove 3 'a': "aaabbbc" => "bbbc"
# 2. Remove 3 'b': "bbbc" => "c"

# Input: "aabbccddeeedcba"
# Output: ""
# Explanation:
# 1. Remove 3 'e': "aabbccddeeedcba" => "aabbccdddcba"
# 2. Remove 3 'd': "aabbccdddcba" => "aabbcccba"
# 3. Remove 3 'c': "aabbcccba" => "aabbba"
# 4. Remove 3 'b': "aabbba" => "aaa"
# 5. Remove 3 'a': "aaa" => ""

def reducer(str):
  stack = [str[0]]

  for idx in range(1, len(str)):
      stack.append(str[idx])

      anchor = idx
      while str[anchor] == str[idx] and anchor > 0:
        anchor -= 1
      
      if str[anchor] != str[idx]: anchor += 1

      numPops = abs(idx-anchor) + 1
      if numPops >= 3:
        for _ in range(numPops):
          stack.pop()
    
  if len(stack) == 0: 
    return ""
  else:
    return separator.join(stack)
