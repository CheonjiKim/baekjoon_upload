import java.util.Scanner; 

public class Main {
	
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		
		int leng = sc.nextInt();
		int value = 0;
		int sum = 0;
		int[] numsArr = new int[leng];
		
		int i, order = 0;

		for (i = 0; i < numsArr.length; i++){
			value = sc.nextInt();
			
			if (value != 0){ // When getting a non-zero value.
				numsArr[order] = value;
				order++;	
			} else{
				order--;
				numsArr[order] = 0;
			}
		}


		for (i = 0; i < numsArr.length; i++) sum += numsArr[i];

		System.out.println(sum);
	}
}
