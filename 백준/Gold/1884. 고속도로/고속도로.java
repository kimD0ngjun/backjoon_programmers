import java.util.*;
import java.io.*;

public class Main {
    private static int N;
    private static int K;
    private static ArrayList<Node>[] graph;

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        K = Integer.parseInt(reader.readLine());
        N = Integer.parseInt(reader.readLine());
        int R = Integer.parseInt(reader.readLine());

        graph = new ArrayList[N + 1];

        for (int i = 1; i <= N; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 0; i < R; i++) {
            StringTokenizer st = new StringTokenizer(reader.readLine());
            int s = Integer.parseInt(st.nextToken());
            int d = Integer.parseInt(st.nextToken());
            int l = Integer.parseInt(st.nextToken());
            int t = Integer.parseInt(st.nextToken());

            // 나름의 최적화
            if (t <= K) {
                graph[s].add(new Node(d, l, t));
            }
        }

        int result = dijkstra();
        System.out.println(result == Integer.MAX_VALUE ? -1 : result);
        reader.close();
    }

    static int dijkstra() {
        Queue<Node> queue = new PriorityQueue<>(Comparator.comparingInt(a -> a.distance));
        int[][] distances = new int[N + 1][K + 1];

        for (int i = 1; i <= N; i++) {
            for (int j = 0; j <= K; j++) {
                distances[i][j] = Integer.MAX_VALUE;
            }
        }

        queue.add(new Node(1, 0, 0));
        distances[1][0] = 0;

        while (!queue.isEmpty()) {
            Node current = queue.poll();
            if (current.distance > distances[current.destination][current.cost]) continue;

            for (Node next : graph[current.destination]) {
                if (current.cost + next.cost > K) continue;
                if (distances[next.destination][current.cost + next.cost] > distances[current.destination][current.cost] + next.distance) {
                    distances[next.destination][current.cost + next.cost] = distances[current.destination][current.cost] + next.distance;
                    queue.add(new Node(next.destination, distances[next.destination][current.cost + next.cost], current.cost + next.cost));
                }
            }
        }

        int minDistance = Integer.MAX_VALUE;
        for (int i = 0; i <= K; i++) {
            minDistance = Math.min(minDistance, distances[N][i]);
        }
        return minDistance;
    }
}

class Node {
    int destination, distance, cost;
    
    Node(int destination, int distance, int cost) {
        this.destination = destination;
        this.distance = distance;
        this.cost = cost;
    }
}
