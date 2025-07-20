class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0) {
            return false;
        }

        String value = String.valueOf(x);

        int left = 0;
        int right = value.length() - 1;
        boolean result = true;

        while (left < right) {
            if (value.charAt(left) != value.charAt(right)) {
                result = false;
                break;
            }

            left++;
            right--;
        }

        return result;
    }
}