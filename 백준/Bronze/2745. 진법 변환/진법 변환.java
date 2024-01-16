import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String input = scanner.nextLine();

        String[] array = input.split(" ");

        int base = Integer.parseInt(array[1]);
        String expression = array[0];
        int length = expression.length() - 1;
        int sum = 0;

        for(char index: expression.toCharArray()) {
            if (!Character.isDigit(index)) {
                int baseNumber = (int) index - 55;
                int value = (int) (baseNumber * Math.pow(base, length));

                sum += value;
                length--;
            } else {
                int baseNumber = Character.getNumericValue(index);
                int value = (int) (baseNumber * Math.pow(base, length));

                sum += value;
                length--;
            }
        }

        System.out.println(sum);
    }
}