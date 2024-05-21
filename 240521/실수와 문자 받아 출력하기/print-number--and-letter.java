import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // 여기에 코드를 작성해주세요.
        char c = sc.next().charAt(0);
        double a = sc.nextDouble();
        double b = sc.nextDouble();
        System.out.printf("%s\n%.2f\n%.2f",c,a,b);
    }
}