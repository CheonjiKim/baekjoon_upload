
import java.util.Scanner;



public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int max, min;
		
		int leng;
		leng = sc.nextInt();
		
		
		int[] arr;
		arr = new int[leng];
		
		
		
		int i;
		for (i = 0; i < leng; i++) {
			int value = sc.nextInt();
			arr[i] = value;
		}
				
		min = arr[0];
		max = arr[0];
		
		for (i = 0; i < leng; i++) {
			
			if (min > arr[i])
				min = arr[i];
			
			if (max < arr[i])
				max = arr[i];
		}
		
		
		System.out.printf("%d %d", min, max);
	}

}
