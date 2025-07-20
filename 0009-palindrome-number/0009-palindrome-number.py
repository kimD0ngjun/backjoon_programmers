class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        value = str(x)

        left = 0
        right = len(value) - 1
        result = True

        while (left < right):
            if value[left] != value[right]:
                result = False
                break
            
            left += 1
            right -= 1
        
        return result
        