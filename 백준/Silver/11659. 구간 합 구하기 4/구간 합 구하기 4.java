//import java.util.Arrays;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N, M;
		N = sc.nextInt();
		M = sc.nextInt();
		sc.nextLine();
		int[] sequenceArr = new int[N]; // 수열 저장
		int[] partialSumArr = new int[N]; // 구간합 저장
 		int[] answerArr = new int[M]; // 정답 저장


		int i;
		for (i = 0; i < N; i++) sequenceArr[i] = sc.nextInt(); // 수열에 값을 담는다.
		sc.nextLine();

		partialSumArr[0] = sequenceArr[0]; // 초항의 구간합 == 초항   
		for (i = 0; i < N - 1; i++) partialSumArr[i + 1] = sequenceArr[i + 1] + partialSumArr[i]; // 구간합을 저장한다.

		//System.out.println(Arrays.toString(sequenceArr)); // 수열에 값 잘 있나 확인하는 코드
		//System.out.println(Arrays.toString(partialSumArr)); // 구간합 수열에 값 잘 있나 확인하는 코드

		for (i = 0; i < M; i++) {
			int startIndex = sc.nextInt() - 1;
			int endIndex = sc.nextInt() - 1;

			// 적절한 구간합을 구해서 정답 배열에 저장한다.
			if (startIndex > 0) 
				answerArr[i] = partialSumArr[endIndex] - partialSumArr[startIndex - 1]; 
			else 
				answerArr[i] = partialSumArr[endIndex];
			}
		for (i = 0; i < M; i++) System.out.println(answerArr[i]); // 정답 출력
	}
}





