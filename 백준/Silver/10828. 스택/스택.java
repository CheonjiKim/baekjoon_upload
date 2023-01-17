
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.util.Scanner;


public class Main {
	
	public static void main(String[] args) throws IOException {

		Scanner sc = new Scanner(System.in);
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int leng = sc.nextInt();
		sc.nextLine();

		String[] commandsArr = new String[leng]; // it will save all the commands from the input 
		String[] resultsArr = new String[leng]; // it will save input numbers by the command 'push X' and delete numbers by the command 'pop'
		
		int i, count = 0;
		for(i = 0; i < commandsArr.length; i++) commandsArr[i] = sc.nextLine(); // Geting all commands into commandsArr.

		for(i = 0; i < commandsArr.length; i++){ // Interpreting all commands in commandsArr. 
			
			if (commandsArr[i].equals("pop")){ // pop's case
				if (count == 0) bw.write("-1\n");
				else {
					count--;
					bw.write(resultsArr[count]+ "\n"); 
					resultsArr[count] = null;
				}
			}
			else if(commandsArr[i].equals("size")){ // size's case
				if (count == 0) bw.write("0\n");
				else bw.write(count + "\n");
			}

			else if(commandsArr[i].equals("empty")){ // empty's case
				if (count == 0) bw.write("1\n");
				else bw.write("0\n");
			}

			else if(commandsArr[i].equals("top")){ // top's case
				if (count == 0) bw.write("-1\n");
				
				else {
					count--;
					bw.write(resultsArr[count] +"\n");
					count++;
				}
			}

			else { // push X's case.
				String numStrOfX = commandsArr[i].substring(5);
				resultsArr[count] = numStrOfX;
				count++;
			}
		}

		bw.flush();
		bw.close();
	}	
}