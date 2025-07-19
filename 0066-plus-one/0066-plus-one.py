from functools import reduce

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        reducer = lambda digits: reduce(lambda acc, d: acc * 10 + d, digits)
        value = reducer(digits) + 1
        
        return list(map(int, str(value)))