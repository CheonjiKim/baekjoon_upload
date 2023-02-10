import java.util.Arrays;
import java.util.StringTokenizer;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		int[] numsArr = new int[N];

		int i;
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		for (i = 0; i < N; i++) numsArr[i] = Integer.parseInt(st.nextToken()); // N개의 수 담기
		Arrays.sort(numsArr); // 정렬하기
		
		int startIndex, endIndex, count = 0;
		// currIndex는 0번째 인덱스부터 N - 1 까지 가야한다.
		// startIndex와 endIndex는 굳이 배열을 다 훑지 않아도 된다. 좋은 수가 맞는 지 아닌지만 따지면 끝난다.
		
		
		for (i = 0; i < N; i++) {
			if (N == 2) break;
			startIndex = 0;
			endIndex = N - 1;
			while (startIndex != endIndex) {
				if (i == startIndex && startIndex < N - 1) startIndex++; // 자기 자신을 포함하여 좋은 수가 되면 안 된다.
				if (i == endIndex && endIndex > 0) endIndex--; // 자기 자신을 포함하여 좋은 수가 되면 안 된다.
				if (startIndex == endIndex) break; // 자기 자신을 포함하여 좋은 수가 되면 안 된다.
				if (numsArr[i]  == numsArr[startIndex] + numsArr[endIndex]) {
					count++;
					break;
				} else if (numsArr[i] < numsArr[startIndex] + numsArr[endIndex]) {
					endIndex--;
				} else if (numsArr[i] > numsArr[startIndex] + numsArr[endIndex]) {
					startIndex++;
				} 
				//System.out.println(i + ": " + startIndex + ": " + endIndex);
				//if (startIndex == endIndex) break;
			}
		}
		System.out.println(count);
	}
}