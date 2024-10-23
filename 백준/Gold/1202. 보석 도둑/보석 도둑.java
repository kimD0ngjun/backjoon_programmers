import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;
import java.util.PriorityQueue;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        String input = reader.readLine();
        String[] info = input.split(" ");

        int N = Integer.parseInt(info[0]);
        int K = Integer.parseInt(info[1]);

        Jewel[] jewels = new Jewel[N];

        for (int i = 0; i < N; i++) {
            String jewel = reader.readLine();
            String[] sequence = jewel.split(" ");
            jewels[i] = new Jewel(Integer.parseInt(sequence[0]), Integer.parseInt(sequence[1]));
        }

        int[] bags = new int[K];

        for (int i = 0; i < K; i++) {
            bags[i] = Integer.parseInt(reader.readLine());
        }

        // 보석 무게 기준 오름차순 정렬
        Arrays.sort(jewels);
        // 가방 무게 기준 오름차순 정렬
        Arrays.sort(bags);

        // 보석 가치 역 우선순위 큐(높은 값부터 뽑게)
        PriorityQueue<Integer> queue = new PriorityQueue<>(Collections.reverseOrder());

        long totalValue = 0;
        int index = 0;

        // 가방 순회
        for (int i = 0; i < K; i++) {
            // 보석 인덱스가 남아있음(보석 순회가 가능) && 현재 가방 무게보다 보석 무게가 덜 나갈 때
            while (index < N && jewels[index].weight <= bags[i]) {
                // 해당 보석 값어치 큐 산입
                queue.add(jewels[index].value);
                index++;
            }

            // 큐에 남아있나?
            if (!queue.isEmpty()) {
                // 현 가방의 무게범위 내의 보석들만 있으니 거기서 가장 값 큰 거 뽑아 더하기
                totalValue += queue.poll();
            }
        }

        System.out.println(totalValue);

    }
}

class Jewel implements Comparable<Jewel> {
    int weight;
    int value;

    public Jewel(int weight, int value) {
        this.weight = weight;
        this.value = value;
    }

    @Override
    // 같으면 0, 첫 번쨰 파라미터가 더 크면 1, 두 번째 파라미터가 더 크면 -1
    public int compareTo(Jewel o) {
        return Integer.compare(this.weight, o.weight);
    }
}