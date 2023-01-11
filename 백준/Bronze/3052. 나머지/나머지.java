import java.util.Scanner; 

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int[] numsArr = new int[10];
		int i, j;
		int DIVISOR = 42; // DIVISOR means '나누는 수' in Korean. 
		
		for (i = 0; i < numsArr.length; i++){
			numsArr[i] = sc.nextInt(); // Input 10 numbers.
			numsArr[i] = numsArr[i] % DIVISOR; // numbers in numsArr are divided by DIVISOR.
		}
		
		// for (i = 0; i < numsArr.length; i++) System.out.println(numsArr[i]);
		
		// numsArr should be sorted to easily find the number of different values.
		// Let's try the bubble sort.



		int temp;
		for(j = 0; j < numsArr.length; j++){
			for (i = 0; i < numsArr.length - (j + 1); i++){
				if (numsArr[i] > numsArr[i + 1]){
					temp = numsArr[i];
					numsArr[i] = numsArr[i + 1];
					numsArr[i + 1] = temp;
					}
			}
		}


		// After sorting, count will increase when a value is different from the next one.
		int count = 1;
		for (i = 0; i < numsArr.length - 1; i++){
			if(numsArr[i] != numsArr[i + 1]) count++;			
		}
		
		System.out.println(count);

	}
}