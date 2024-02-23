class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = self.find_pivot(nums)
        if pivot == -1:
            return self.binary_search(nums, target, 0, len(nums) - 1)
        
        if nums[pivot] == target:
            return pivot
        elif nums[0] <= target:
            return self.binary_search(nums, target, 0, pivot - 1)
        else:
            return self.binary_search(nums, target, pivot + 1, len(nums) - 1)
        
    def find_pivot(self, nums):
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            mid = (low + high) // 2
            if mid < high and nums[mid] > nums[mid + 1]:
                return mid
            elif mid > low and nums[mid] < nums[mid - 1]:
                return mid - 1
            elif nums[low] >= nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return -1
    
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
