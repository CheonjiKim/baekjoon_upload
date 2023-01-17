import java.util.Scanner;
//import java.io.*;

public class Main {
	
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		
		int leng = sc.nextInt();
		String[] stringsArr = new String[leng];
		String[] yesNoArr = new String[leng];
		String eachLine;
		//System.out.println(stringsArr.length);		

		int i, j, count;
		
		// getting string values.
		for(i = 0; i < stringsArr.length; i++) stringsArr[i] = sc.next();

		for (i = 0; i < stringsArr.length; i++){
			count = 0;
			eachLine = stringsArr[i];
			String[] charsInOneLineArr = new String[eachLine.length()];


			// Saving each single character in the charsInOnLineArr.
			for (j = 0; j < eachLine.length(); j++) charsInOneLineArr[j] = eachLine.substring(j, j + 1);
		

			for(j = 0; j < eachLine.length(); j++){
				// If "(", add 1 to count. Else, add -1 to count.
				// A proper VPS does not make count under zero.
				if (charsInOneLineArr[j].equals("(")) count += 1;
				else count += -1;

				
				// If count ever gets under zero, the string is not a proper VPS: "NO".
				if (count < 0){
					yesNoArr[i] = "NO";
					break;
				}
				else yesNoArr[i] = "YES";
			}
			
			// if count in the end is not zero, the string is not a proper VPS: "NO".
			if (count != 0) yesNoArr[i] = "NO";
		}
		for (i = 0; i < stringsArr.length; i++) System.out.println(yesNoArr[i]);
	}	
}
