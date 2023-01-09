
import java.util.Scanner;



public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int max;
		int locationOfMax = 0;
		
		int leng = 9;
		
		
		int[] arr;
		arr = new int[leng];
		
		
		
		int i;
		for (i = 0; i < leng; i++) {
			int value = sc.nextInt();
			arr[i] = value;
		}
		
		max = arr[0];
		
		for (i = 0; i < leng; i++) {
			
			if (max <= arr[i]) { // max < arr[i]논 논리 오류 발생한다. 0번째 배열이 최댓값이면 locationOfMax == 0이된다.
				max = arr[i];
				locationOfMax = (i + 1);
			}
		}
		
		
		System.out.println(max);
		System.out.println(locationOfMax);
	}

}