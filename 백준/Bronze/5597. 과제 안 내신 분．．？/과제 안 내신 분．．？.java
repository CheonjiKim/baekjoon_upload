import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int[] attStuArr, arr30;
		attStuArr = new int[28];
		arr30 = new int[30];

		int i, j;
		for(i = 0; i < arr30.length; i++) arr30[i] = i + 1; // Assigning numbers from 1 to 30 into arr30.
		for(i = 0; i < attStuArr.length; i++) attStuArr[i] = sc.nextInt(); // Getting and assigning attended students' number into arrStuArr.
		
		for (i = 0; i < attStuArr.length; i++){
			for(j = 0; j < arr30.length; j++){
				if (attStuArr[i] == arr30[j]) arr30[j] = 0; // arr30 will have two absent students' numbers. Other numbers(attended students' numbers) in arr30 will become zero.
			}
		}
		
		for (i = 0; i < arr30.length; i++){
			if (arr30[i] != 0) System.out.println(arr30[i]);
		}
	}
}