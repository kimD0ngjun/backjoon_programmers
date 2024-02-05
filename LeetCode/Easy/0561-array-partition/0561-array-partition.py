class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()  # 크기 순서대로 배열 재정렬
        total_sum = 0

        for i in range(0, len(nums), 2):
            total_sum += min(nums[i], nums[i + 1])

        return total_sum
