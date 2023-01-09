import java.util.Scanner;



public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int leng;
		leng = sc.nextInt();
		
	
		int[] arr;
		arr = new int[leng];
		
		
		
		int i;
		for (i = 0; i < leng; i++) { // 배열에 값을 담는 과
			int value = sc.nextInt();
			arr[i] = value;
		}
		
		int findNum;
		findNum = sc.nextInt();
		int count = 0;
		for (i = 0; i < leng; i++) {
			if(arr[i] ==findNum)
				count++;
		}
		
		System.out.println(count);

	}

}