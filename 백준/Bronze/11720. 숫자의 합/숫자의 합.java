import java.util.Scanner;

public class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);

        int testcase = sc.nextInt();
        int sum = 0;
        String nums;
        sc.nextLine();
        nums = sc.nextLine();

        int i;
        for (i = 0; i < testcase; i++) sum += Integer.parseInt(nums.substring(i, i+1));
        System.out.println(sum);
    }
}   