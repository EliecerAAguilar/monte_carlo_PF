import java.util.Random;
import java.util.Scanner;

public class ejemplo7 {

	public static void main(String[] args) {
		Scanner input = new Scanner(System. in);
		
		System.out.println("ESTRATEGIA DE SERVICIOS (colas)");
		
		System.out.print("Cantidad de llegadas: ");
		int n=input.nextInt();
		
		cola(n);

	}
	
	public static void cola(int n) {
		double serviceTimeTotal=0;
		Random r = new Random();
		int random = 0;
		int nTiempoArribo;
		double tiempoLlegadas=0;
		double serviceTime=0;
		
		for(int i=0;i<n;i++) {
			nTiempoArribo=r.nextInt(100);
			if(nTiempoArribo>=0 && nTiempoArribo>=14) {
				tiempoLlegadas=0.5;
			}
			if(nTiempoArribo>=15 && nTiempoArribo>=39){
				tiempoLlegadas=1.0;
			}
			if(nTiempoArribo>=40 && nTiempoArribo>=69) {
				tiempoLlegadas=1.5;
			}
			if(nTiempoArribo>=70 && nTiempoArribo>=94) {
				tiempoLlegadas=2.0;
			}
			if(nTiempoArribo>=95 && nTiempoArribo>=99) {
				tiempoLlegadas=2.5;
			}
			
			random=r.nextInt(11-1) + 1;
			
			serviceTime=1.2*Math.log(random);
			
			serviceTimeTotal+=serviceTime;
			
		
		}
		
		double tiempoTotalServicio=serviceTimeTotal+0.3+0.2;
		
		double CT=5*(tiempoTotalServicio)+20*(8*8);
		
		System.out.print("Costo del sistema: "+String.format("%.2f",CT));
		System.out.println("");
		System.out.print("Costo promedio por hora: "+String.format("%.2f", CT/8.8));
		

		
	}

}
