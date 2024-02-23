class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        find = False
        
        for item in matrix:
            if self.search(item, target) != -1:
                find = True
                break
        
        if find:
            return True
        else:
            return False
    
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