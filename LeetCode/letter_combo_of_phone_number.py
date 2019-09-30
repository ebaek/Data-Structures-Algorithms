# 17: Letter Combinations of a Phone Number

# Approach:
# put all the phone numbers and the combinations in a dictionary 
# in a helper method, explore all the combinations of the first digit in remaining digits
# base case is if the length of remaining digits is 0, just append with combos
# otherwise, keep exploring, shorten the recursive number of combinations 

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {"2": ("a", "b", "c"), "3": ("d", "e", "f"), "4": ("g", "h", "i"),
                 "5": ("j", "k", "l"), "6": ("m", "n", "o"), "7": ("p", "q", "r", "s"),
                 "8": ("t", "u", "v"), "9": ("w", "x", "y", "z")}

        combos = []

        def helper(combo, remaining_digits):
            if len(remaining_digits) == 0:
                combos.append(combo)
            else:
                for digit in phone[remaining_digits[0]]:
                    helper(combo + digit, remaining_digits[1:])

        if digits:
            helper("", digits)
        return combos
