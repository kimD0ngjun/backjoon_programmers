import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 입력 처리
        int[][] sudoku = new int[9][9];
        List<int[]> blanks = new ArrayList<>();

        // 입력 받기
        for (int i = 0; i < 9; i++) {
            String line = br.readLine();
            String[] numbers = line.split(" ");

            for (int j = 0; j < 9; j++) {
                sudoku[i][j] = Integer.parseInt(numbers[j]);
                if (sudoku[i][j] == 0) {
                    blanks.add(new int[]{i, j});
                }
            }
        }

        // 풀이
        SudokuSolver solver = new SudokuSolver(sudoku, blanks);
        solver.solve();

        // 버퍼 정리
        br.close();
    }
}

class SudokuSolver {
    private final int[][] sudoku;
    private final List<int[]> blanks;
    private final List<Set<Integer>> rowMemo = new ArrayList<>(9);
    private final List<Set<Integer>> columnMemo = new ArrayList<>(9);
    private final List<Set<Integer>> moduleMemo = new ArrayList<>(9);

    public SudokuSolver(int[][] sudoku, List<int[]> blanks) {
        this.sudoku = sudoku;
        this.blanks = blanks;

        // Initialize lists with empty sets
        for (int i = 0; i < 9; i++) {
            this.rowMemo.add(new HashSet<>());
            this.columnMemo.add(new HashSet<>());
            this.moduleMemo.add(new HashSet<>());
        }

        this.initialize();
    }

    // 메모이제이션 초기화
    private void initialize() {
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                int number = this.sudoku[i][j];

                if (number != 0) {
                    this.rowMemo.get(i).add(number);
                    this.columnMemo.get(j).add(number);

                    int moduleIndex = (i / 3) * 3 + (j / 3);
                    this.moduleMemo.get(moduleIndex).add(number);
                }
            }
        }
    }

    // 계산
    public void solve() throws IOException {
        this.calculate(0);
    }

    private boolean calculate(int n) throws IOException {
        if (n >= this.blanks.size()) {
            this.printSudoku();
            System.exit(0);
        }

        int[] currentBlank = this.blanks.get(n);
        int x = currentBlank[0];
        int y = currentBlank[1];
        int moduleIndex = (x / 3) * 3 + (y / 3);

        for (int num = 1; num < 10; num++) {
            if (
                    !this.rowMemo.get(x).contains(num) &&
                            !this.columnMemo.get(y).contains(num) &&
                            !this.moduleMemo.get(moduleIndex).contains(num)
            ) {
                this.sudoku[x][y] = num;
                this.rowMemo.get(x).add(num);
                this.columnMemo.get(y).add(num);
                this.moduleMemo.get(moduleIndex).add(num);

                if (calculate(n + 1)) return true;

                this.sudoku[x][y] = 0;
                this.rowMemo.get(x).remove(num);
                this.columnMemo.get(y).remove(num);
                this.moduleMemo.get(moduleIndex).remove(num);
            }
        }

        return false;
    }

    private void printSudoku() throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        for (int[] ints : this.sudoku) {
            for (int anInt : ints) {
                bw.write(anInt + " ");
            }
            bw.newLine();
        }

        bw.flush();
        bw.close();
    }
}
