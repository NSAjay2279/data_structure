import java.util.Scanner;

public class Roots {
	public static void main(String[] args) {
		double a,b,c,r1,r2,y,z,w;
		Scanner scan = new Scanner(System.in);
		a = scan.nextDouble();
		b = scan.nextDouble();
		c = scan.nextDouble();
		y = b*b - 4*a*c;
		w = 2*a;
		if(y==0)
			System.out.println("Equal roots = " + -b/w);
		else
			if (y < 0)
				System.out.println("Complex roots \n");
			else
			{
				z = Math.sqrt(y);
				r1 = (-b-z)/w;
				r2 = (-b+z)/w;
				System.out.println("root1 = " + r1 + ", root2 = " + r2);
			}
			scan.close();
	}
}