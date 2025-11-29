import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String strN = br.readLine();
        int N = Integer.parseInt(strN);
        
        for (int i=1; i<=N; i++) {
            for (int j=0; j<i; j++) {
                System.out.print("*");
            }
            System.out.print("\n");
        }
    }
}