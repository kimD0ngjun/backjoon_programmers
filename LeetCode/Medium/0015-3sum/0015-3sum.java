class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();

        if (nums == null || nums.length < 3) {
            return result;
        }

        Arrays.sort(nums);

        for (int i = 0; i < nums.length - 2; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            } // 중복 값이면 건너뛰기

            int left = i + 1; // 바로 다음 값
            int right = nums.length - 1; // 마지막 값
            // 이 두 사이 훑으면서 값 탐색

            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];

                if (sum == 0) {
                    result.add(Arrays.asList(nums[i], nums[left], nums[right]));

                    while (left < right && nums[left] == nums[left + 1]) {
                        left++; // left 훑는 중에 중복 값 건너뛰기
                    }
                    while (left < right && nums[right] == nums[right - 1]) {
                        right--; // right 훑는 중에 중복 값 건너뛰기
                    }

                    left++;
                    right--;
                } else if (sum < 0) {
                    left++;
                } else if (sum > 0) {
                    right--;
                }
            }
        }

        return result;
    }
}