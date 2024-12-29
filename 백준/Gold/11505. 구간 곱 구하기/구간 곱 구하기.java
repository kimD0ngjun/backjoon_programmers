import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        long[] arr = new long[N];

        for (int i = 0; i < N; i++) {
            arr[i] = Long.parseLong(br.readLine());
        }

        SegmentTree segmentTree = new SegmentTree(arr);

        for (int i = 0; i < (M + K); i++) {
            st = new StringTokenizer(br.readLine());

            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            long c = Long.parseLong(st.nextToken());

            if (a == 1) {
                segmentTree.updateValue(b - 1, c);
            } else {
                System.out.println(segmentTree.getRangeSum(b - 1, (int) c - 1));
            }
        }
    }
}
class SegmentTree {
    private final long[] tree; // 세그먼트 트리를 저장할 배열
    private final int n; // 원본 배열 크기
    private static final long MOD = 1_000_000_007;

    public SegmentTree(long[] arr) {
        n = arr.length;
        tree = new long[n * 4];
        buildTree(arr, 0, n - 1, 1);
    }

    private void buildTree(long[] arr, int start, int end, int node) {
        if (start == end) { // 리프 노드
            tree[node] = arr[start] % MOD;
            return;
        }

        int mid = (start + end) / 2;

        buildTree(arr, start, mid, node * 2); // 왼쪽 자식
        buildTree(arr, mid + 1, end, node * 2 + 1); // 오른쪽 자식

        tree[node] = (tree[node * 2] * tree[node * 2 + 1]) % MOD;
    }

    public long getRangeSum(int left, int right) {
        return query(0, n - 1, 1, left, right);
    }

    private long query(int start, int end, int node, int left, int right) {
        if (right < start || end < left) { // 범위 밖
            return 1; // 항등원
        }

        if (left <= start && end <= right) { // 범위 안
            return tree[node];
        }

        int mid = (start + end) / 2;

        return (query(start, mid, node * 2, left, right) *
                query(mid + 1, end, node * 2 + 1, left, right)) % MOD;
    }

    public void updateValue(int index, long newValue) {
        update(0, n - 1, 1, index, newValue);
    }

    private void update(int start, int end, int node, int index, long newValue) {
        if (start == end) {
            tree[node] = newValue % MOD;
            return;
        }

        int mid = (start + end) / 2;

        if (index <= mid) { // 왼쪽 자식
            update(start, mid, node * 2, index, newValue);
        } else { // 오른쪽 자식
            update(mid + 1, end, node * 2 + 1, index, newValue);
        }

        tree[node] = (tree[node * 2] * tree[node * 2 + 1]) % MOD;
    }
}
