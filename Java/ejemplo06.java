import java.util.Random;
import java.util.Scanner;

public class ejemplo6 {

	public static void main(String[] args) {
		Scanner input = new Scanner(System. in);
	
		System.out.println("SIMULACI�N DEL TAMBALEO DEL BORRACHO");
		
		System.out.print("Ingrese cantidad de pasos: ");
		
		int n = input.nextInt();
		
		borracho(n);

	}
	
	public static void borracho(int n) {
		int x=0,y=0;
		Random r = new Random();
		int random = 0;
		
		for(int i=0;i<n;i++) {
			random=r.nextInt(101-1) + 1;
			 if(random>=0 && random<25) {
				 y+=1;
			 }
			 
			 if(random>=25 && random<50) {
				 y-=1;
			 }        
			 
			 if(random>=50 && random<75) {
				 x+=1;
			 }
			 if(random>=75 && random<100) {
				 x-=1;
			 }
			 System.out.println("Coordenadas (X,Y)");
			 System.out.println("("+x+","+y+")");
		}
		
		if(Math.abs(x+y)>=2) {
			System.out.println("El borracho termino a 2 o mas cuadras de donde estaba inicialmente.");
		}
		else {
			System.out.println("El borracho termino a menos de 2 cuadras de donde estaba inicialmente.");
		}
	}

}
