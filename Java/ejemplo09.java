import java.util.Random;
import java.util.Scanner;

public class ejemplo9 {

	public static void main(String[] args) {
		double pTeorica = 0.49228;
		
		Scanner input = new Scanner(System. in);
		
		System.out.print("N�mero de corridas: ");
		double n=input.nextDouble();
		
		double wins=cramp(n);
		
		double pExperimental=wins/n;
	
		double error=Math.abs((pExperimental-pTeorica)/pTeorica)*100;
		
		System.out.println("La probabilidad de ganar el juego es de: "+pExperimental);
		
		System.out.println("Teoricamente est� probabildiad es de "+pTeorica+" donde comparando con la simulaci�n tenemos un error de: "+error);
		
	}
	
	public static double cramp(double n) {
		double wins=0;
		
		for(int i=0;i<n;i++) {
			wins=wins+singleCramp();
		}
		
		return wins;
	}
	
	public static int singleCramp() {
		Random r = new Random();
		int dice1=r.nextInt(7-1) + 1;
		int dice2=r.nextInt(7-1) + 1;
		int sum1=dice1+dice2;
		int returnValue=0;
		boolean foo;
		
		if(sum1==7 || sum1==11){
			returnValue=1;
		}
		
		else if(sum1==2 || sum1==3 || sum1==12) {
			returnValue=0;
		}
		else {
			foo=true;
			
			while(foo==true) {
				dice1=r.nextInt(7-1) + 1;
				dice2=r.nextInt(7-1) + 1;
				int sum2=dice1+dice2;
				if(sum2==sum1) {
					foo=false;
					returnValue=1;
				}
				else if(sum2==7) {
					foo=false;
					returnValue=0;
				}
			}
			
		}
		
		return returnValue;
	}
	
	
	
	

}
