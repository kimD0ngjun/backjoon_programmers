class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_dict = {}
        
        for i in range(len(nums)):
            value = target - nums[i]
            
            if value in index_dict:
                return [index_dict[value], i]
            
            index_dict[nums[i]] = i