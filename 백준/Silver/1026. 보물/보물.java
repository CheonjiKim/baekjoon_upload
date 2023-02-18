import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;


public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		sc.nextLine();
		int[] A = new int[N];
		int[] B = new int[N];
		Integer[] C = new Integer[N];
		int sum = 0;
		
		int i;
		for (i = 0; i < N; i++) A[i] = sc.nextInt();
		sc.nextLine();
		for (i = 0; i < N; i++) {
			B[i] = sc.nextInt(); 
			C[i] = B[i];
		} 
		Arrays.sort(A);
		Arrays.sort(C, Collections.reverseOrder());
		// System.out.println(Arrays.toString(A));
		// System.out.println(Arrays.toString(B));
		// System.out.println(Arrays.toString(C));
		for (i = 0; i < N; i++) sum += A[i] * C[i];
		System.out.println(sum);
	}
}