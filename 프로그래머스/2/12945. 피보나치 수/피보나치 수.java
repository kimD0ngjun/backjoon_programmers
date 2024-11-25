class Solution {
    private static final int MOD = 1_234_567;

    public int solution(int n) {
        int[] result = new int[]{1, 0, 0, 1};
        int[] unit = new int[]{1, 1, 1, 0};

        while (n > 0) {
            if (n % 2 == 1) result = matrix(result, unit);
            n /= 2;
            unit = matrix(unit, unit);
        }

        return result[1];
    }

    public int[] matrix(int[] a, int[] b) {
        int r1 = (int)(((long)a[0] * b[0] + (long)a[1] * b[2]) % MOD);
        int r2 = (int)(((long)a[0] * b[1] + (long)a[1] * b[3]) % MOD);
        int r3 = (int)(((long)a[2] * b[0] + (long)a[3] * b[2]) % MOD);
        int r4 = (int)(((long)a[2] * b[1] + (long)a[3] * b[3]) % MOD);

        return new int[]{r1, r2, r3, r4};
    }

//    public static void main(String[] args) {
//        Solution solution = new Solution();
//        System.out.println(solution.solution(5));
//    }
}