import java.util.Scanner;

public class ejemplo8 {

	public static void main(String[] args) {
Scanner input = new Scanner(System. in);

		System.out.print("Cantidad de n�meros a generar: ");
		int ctdNums=input.nextInt();
		
		double [] r=genUnif(ctdNums);
		
		double lmb=0.5;
		
		double [] randomNumbers=genExpo(r,lmb,ctdNums);
		
		for(int i=0;i<ctdNums;i++) {
			System.out.println(randomNumbers[i]);
		}
	}
	
	public static double [] genUnif(int ctdNums) {
		double randNums[] = new double[ctdNums];
		
		for(int i=0;i<ctdNums;i++) {
			randNums[i]=Math.random();
		}
		
		return randNums;
	}
	
	public static double [] genExpo(double [] r,double lmb,int ctdNums) {
		double [] lista=new double[ctdNums];
		double x;			
		for(int i=0;i<ctdNums;i++) {
			x=-(1/lmb)*(Math.log(r[i]));
			lista[i]=x;
		}
		
		return lista;
	}

}
