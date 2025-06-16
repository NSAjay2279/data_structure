import java.util.Scanner;

public class Max {
	public static void main(String[] args) {
		int n, max, number;
		Scanner scan = new Scanner(System.in);
		n = scan.nextInt();
		if (n > 0) {
			number = scan.nextInt();
			max = number;
			for (int i = 1; i <n; i++) {
				number = scan.nextInt();
				if (number > max) max = number;
			}
			System.out.println("MAX = " + max);
			scan.close();
		}

	}
}