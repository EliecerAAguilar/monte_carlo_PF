import java.util.Random;
import java.util.Scanner;

public class ejemplo5 {

	public static void main(String[] args) {
		Scanner input = new Scanner(System. in);
		
		System.out.println("APROXIMACI�N DEL N�MERO PI");
		
		System.out.print("Longitud de la aguja(l): ");
		double lon=input.nextDouble();
		
		System.out.print("Cantidad de lazamientos: ");
		double n=input.nextDouble();
		
		double valorPi=aproxPI(lon,n);
		
		System.out.println("Valor aproximado de PI: "+valorPi);

	}
	
	public static double aproxPI(double lon,double n) {
		int aciertos=0;
		double r1,x,r2,y,vpi;
	
		for(int i=0;i<n;i++) {
			r1=Math.random();
			x=r1*(lon/2.0);
			r2=Math.random();
			y=(lon/2.0)*Math.sin(180*r2);
			
			if(x<=y) {
				aciertos+=1;
			}
	
		}
		
		
		System.out.println("Aciertos: "+aciertos);
		
		vpi=n/aciertos;
		
		return vpi;
	}

}
