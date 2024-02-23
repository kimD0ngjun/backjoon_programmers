from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = []

        for i in range(len(numbers)):
            another_target = target - numbers[i]

            j = self.search(numbers, another_target)

            if j != -1 and j != i:
                result.append(i + 1)
                result.append(j + 1)
                break

        result.sort()

        return result

    # 이진 탐색 메소드
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, target, 0, len(nums) - 1)

    def binary_search(self, nums, target, low_index, high_index):
        if low_index > high_index:
            return -1

        middle_index = (low_index + high_index) // 2

        if nums[middle_index] == target:
            return middle_index
        elif nums[middle_index] > target:
            return self.binary_search(nums, target, low_index, middle_index - 1)
        else:
            return self.binary_search(nums, target, middle_index + 1, high_index)
