import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[] arr = new int[N];

        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        SegmentTree tree = new SegmentTree(arr);

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());

            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            Node node = tree.getRangeMaximum(a - 1, b - 1);
            System.out.println(node.min);

//            System.out.println();
        }

        br.close();
    }
}

class SegmentTree {
    final Node[] tree;
    final int n;

    public SegmentTree(int[] arr) {
        n = arr.length;
        tree = new Node[n * 4];
        for (int i = 0; i < tree.length; i++) {
            // 각 노드가 독립적인 객체를 가지도록 설정
            // Arrays.fill()을 쓰면 모든 인덱스가 같은 객체를 참조해버림
            tree[i] = new Node(Integer.MAX_VALUE);
        }
        buildTree(arr, 0, n - 1, 1);
    }

    private void buildTree(int[] arr, int start, int end, int node) {
        if (start == end) { // 리프 노드
            tree[node] = new Node(arr[start]);
            return;
        }

        int mid = (start + end) / 2;

        buildTree(arr, start, mid, node * 2); // 왼쪽 자식
        buildTree(arr, mid + 1, end, node * 2 + 1); // 오른쪽 자식

        tree[node] = new Node(
                Math.min(tree[node * 2].min, tree[node * 2 + 1].min));
    }

    public Node getRangeMaximum(int left, int right) {
        return query(0, n - 1, 1, left, right);
    }

    /**
     * @param start : 시작 범위
     * @param end : 끝 범위
     * @param node : 탐색 시작 인덱스
     * @param left : 탐색 범위 시작
     * @param right : 탐색 범위 끝
     * @return : 탐색 대상 노드
     */
    private Node query(int start, int end, int node, int left, int right) {
        if (right < start || end < left) { // 범위 밖
            return new Node(Integer.MAX_VALUE); // 최댓값의 항등원?
        }

        if (left <= start && end <= right) { // 범위 안
            return tree[node];
        }

        int mid = (start + end) / 2;

        Node leftNode = query(start, mid, node * 2, left, right);
        Node rightNode = query(mid + 1, end, node * 2 + 1, left, right);

        return new Node(Math.min(leftNode.min, rightNode.min));
    }
}

class Node {
    int min;

    public Node(int min) {
        this.min = min;
    }
}