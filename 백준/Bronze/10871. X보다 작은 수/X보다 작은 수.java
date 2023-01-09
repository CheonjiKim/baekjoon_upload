import java.util.Scanner;



public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int leng;
		leng = sc.nextInt();
		
		int X;
		X = sc.nextInt();
		
		
		int[] arr;
		arr = new int[leng];
		
		
		
		int i;
		for (i = 0; i < leng; i++) {
			int value = sc.nextInt();
			arr[i] = value;
		}
				
			for (i = 0; i < leng; i++) {
			if(arr[i] < X)
				System.out.printf("%d ", arr[i]);
			
			
		}
		
		

	}

}