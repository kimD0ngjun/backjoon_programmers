class Solution:
    def isPalindrome(self, s: str) -> bool:

        """
        공백 최적화
        printable ASCII 판별 최적화
        """
        lower_s = ''.join(char for char in s if char not in string.punctuation and not char.isspace()).lower()

        # 투 포인터 인덱스
        left = 0
        right = len(lower_s) - 1

        while left < right:

            if lower_s[left] != lower_s[right]:
                return False

            left += 1
            right -= 1

        return True