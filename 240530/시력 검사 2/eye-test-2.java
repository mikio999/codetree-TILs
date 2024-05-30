import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // 여기에 코드를 작성해주세요.
        double a = sc.nextDouble();
        if (a >= 1.0) {
            System.out.println("High");
        }
        else if (a >= 0.5) {
            System.out.println("Middle");
        }
        else {
            System.out.println("Low");
        }
    }
}