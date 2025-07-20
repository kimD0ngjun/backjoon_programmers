import java.util.*;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> indexMap = new HashMap<>();
        
        for (int i = 0; i < nums.length; i++) {
            int value = target - nums[i];
            
            if (indexMap.containsKey(value)) {
                return new int[] { indexMap.get(value), i };
            }
            
            indexMap.put(nums[i], i);
        }

        throw new IllegalArgumentException();
    }
}