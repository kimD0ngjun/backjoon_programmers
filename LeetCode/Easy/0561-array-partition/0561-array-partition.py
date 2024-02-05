class Solution {
    public int arrayPairSum(int[] nums) {
        Arrays.sort(nums); // 크기 순서대로 배열 재정렬
        int sum = 0;

        for (int i = 0; i < nums.length/2; i++) {
            int min = Math.min(nums[2*i], nums[2*i + 1]);

            sum += min;
        }

        return sum;
    }
}