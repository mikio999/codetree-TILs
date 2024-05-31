import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();

        switch (a) {
            case "S":
                System.out.println("Superior");
                break;
            case "A":
                System.out.println("Excellent");
                break;
            case "B":
                System.out.println("Good");
                break;
            case "C":
                System.out.println("Usually");
                break;
            case "D":
                System.out.println("Effort");
                break;
            default:
                System.out.println("Failure");
                break;
        }
    }
}