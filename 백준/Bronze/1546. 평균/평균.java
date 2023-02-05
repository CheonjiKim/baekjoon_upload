import java.util.Scanner;

public class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);

        int testcase = sc.nextInt();
        float max = 0;
        float average = 0;
        sc.nextLine();
        float[] scoresArr = new float[testcase];

        int i;
        for (i = 0; i < testcase; i++) { // 점수를 배열에 저장
            scoresArr[i] = sc.nextInt();
            //System.out.println(scoresArr[i]);      
        }

        for (i = 0; i < testcase; i++) { // 최댓값 찾는 과정
            if (scoresArr[i] > max) max = scoresArr[i];
        }
        //System.out.println(max);

        for (i = 0; i < testcase; i++) { // 점수 조작하는 과정
            scoresArr[i] = scoresArr[i] / max * 100; 
            //System.out.println(scoresArr[i]);
            average += scoresArr[i];
        }

        System.out.println(average / testcase); 
    }
}  