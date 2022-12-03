import java.util.Random;
import java.util.Scanner;

public class ejemplo4 {

	public static void main(String[] args) {
		Scanner input = new Scanner(System. in);
		
		System.out.println("�REA BAJO LA CURVA");
		
		System.out.print("Limite inferior (a): ");
		double a = input.nextDouble();
		
		System.out.print("Limite inferior (b): ");
		double b = input.nextDouble();
		
		System.out.print("Valor m�ximo (fmax): ");
		double fmax = input.nextDouble();
		
		System.out.print("N�meros de puntos a simular: ");
		int n = input.nextInt();
		
		n=n+1;
		
		double resultado=calcularArea(a,b,fmax,n);
		
		System.out.println("Area aproximada: "+resultado);
		
	}
	
	public static double calcularArea(double a, double b, double fmax, int n) {
		
		double area=0.0;
		double aciertos=0;
		double r1,xi,fxi,r2,yi;
		String acierto="";
		
		System.out.println("r1 || x || f(x) || r2 || y || aciertos");
		
		for(int i=0;i<=n;i++) {
			r1=Math.random();
			xi=r1*(b-a)+a;
			fxi=Math.sin(Math.PI*xi)/(Math.PI*xi);
			r2=Math.random();
			yi=r2*fmax;
			
			if(yi<=fxi) {
				aciertos=aciertos+1;
				acierto="Y";
			}
			else {
				acierto="N";
			}
			
			System.out.println(r1+" || "+xi+" || "+fxi+" || "+r2+" || "+yi+" || "+acierto);
		}
		
		System.out.println("Valor Aciertos: "+aciertos);
		System.out.println("Valor n: "+n);
		System.out.println("Valor a: "+a);
		System.out.println("Valor b: "+b);
		
		area=(aciertos/(n))*(b-a);
		
		System.out.println("Area aproximada antes de: "+area);
		
		return area;
	}

}
