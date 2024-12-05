import java.io.*;
import java.util.*;

public class Main {
    private static final int INF = Integer.MAX_VALUE;

    private static int N;
    private static Map<Integer, Map<Integer, Integer>> graph;
    private static int[] distances;
    private static List<HashSet<Integer>> prevNodes; // 해당 노드(인덱스)들에 저장하기 위한 직전 노드 저장
    private static boolean[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        List<Integer> results = new ArrayList<>();

        while (true) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());

            if (N == 0 && m == 0) break;

            st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int d = Integer.parseInt(st.nextToken());

            // 그래프 초기화
            graph = new HashMap<>();
            distances = new int[N];
            prevNodes = new ArrayList<>();
            visited = new boolean[N];

            for (int i = 0; i < N; i++) {
                distances[i] = INF; // 최단 거리 초기화
                prevNodes.add(new HashSet<>()); // 이전 노드 저장용 Set 초기화
            }

            // 그래프 입력
            for (int i = 0; i < m; i++) {
                st = new StringTokenizer(br.readLine());
                int u = Integer.parseInt(st.nextToken());
                int v = Integer.parseInt(st.nextToken());
                int p = Integer.parseInt(st.nextToken());

                graph.putIfAbsent(u, new HashMap<>());
                graph.get(u).put(v, p); // 방향 그래프
            }

            dijkstra(s); // 최단 경로(들) 찾고
            bfs(d); // 최단 경로(들) 삭제하고
            dijkstra(s); // 다음 최단 경로인 '거의 최단 경로' 다시 찾기

            results.add(distances[d]);
        }

        for (int result : results) {
            System.out.println(result == INF ? -1 : result);
        }

        br.close();
    }

    static void dijkstra(int start) {
        PriorityQueue<Node> queue = new PriorityQueue<>();
        Arrays.fill(visited, false); // 방문 배열 초기화
        Arrays.fill(distances, INF); // 거리 배열 초기화
        distances[start] = 0; // 시작점까지의 거리는 0

        queue.add(new Node(start, 0));

        while (!queue.isEmpty()) {
            Node current = queue.poll();

            /**
             * 나름의 최적화
             */
            if (visited[current.city]) continue; // 이미 방문한 노드는 스킵
            visited[current.city] = true; // 방문 처리

            if (!graph.containsKey(current.city)) continue; // 인접 노드가 없는 경우 스킵

            /**
             * 탐색 시작
             */
            for (Map.Entry<Integer, Integer> entry : graph.get(current.city).entrySet()) {
                int next = entry.getKey();
                int nextDistance = entry.getValue();

                if (visited[next]) continue; // 이미 방문한 노드는 스킵

                int distance = distances[current.city] + nextDistance;

                if (distance < distances[next]) {
                    // 새로운 최단 거리 발견 케이스
                    distances[next] = distance;
                    queue.add(new Node(next, distance));
                    prevNodes.get(next).clear(); // 이전 경로 삭제
                    prevNodes.get(next).add(current.city); // 새로운 단기 경로 추가
                } else if (distance == distances[next]) {
                    prevNodes.get(next).add(current.city); // 같은 거리의 경로는 추가
                }
            }
        }
    }

    // 최단 경로 삭제(가중치 무한대로 업데이트)
    static void bfs(int destination) {
        Queue<Integer> queue = new LinkedList<>();
        boolean[] visitedForDelete = new boolean[N];

        queue.add(destination);
        visitedForDelete[destination] = true; // 목적지까지의 최단 경로 간선 삭제 처리

        while (!queue.isEmpty()) {
            int current = queue.poll();

            for (int prev : prevNodes.get(current)) {
                // 직전 노드가 존재하고 직전 노드에서 현재 노드로 가는 간선이 존재하는(얘는 최단경로만 삭제하려고)
                if (graph.containsKey(prev) && graph.get(prev).containsKey(current)) {
                    graph.get(prev).remove(current); // 최단 경로 간선 삭제
                    if (!visitedForDelete[prev]) {
                        queue.add(prev); // prev -> current
                        visitedForDelete[prev] = true;
                    }
                }
            }
        }
    }
}

class Node implements Comparable<Node> {
    int city, distance;

    Node(int city, int distance) {
        this.city = city;
        this.distance = distance;
    }

    @Override
    public int compareTo(Node other) {
        return this.distance - other.distance;
    }
}