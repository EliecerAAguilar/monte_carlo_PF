import java.util.ArrayList;

public class ejemplo1 {

	public static void main(String[] args) {
		ArrayList<Integer> x= new ArrayList<Integer>();
		
		for(int i=1;i<=100;i++) {
			x.add(i);
		}
		
		ArrayList<Integer> yDesc=tDescompuesto(x);
		
		ArrayList<Integer> yRepar=tReparacion(x);
		
		simulacion(x,yDesc,yRepar);

	}

	public static void simulacion(ArrayList<Integer> x, ArrayList<Integer> yDesc, ArrayList<Integer> yRepar) {
		int [] randomDes = {83,97,88,12,22,16,24,64,37,62,52,9,64,74,15,47,86,79,43,35};
		int [] randomRepar = {91,4,72,12,30,32,91,29,33,8,25,74,97,70,15,43,42,25,71,14};
		double tDescompostura=0;
		double tInicioReparacion=0;
		double tEsperaMaquina=0;
		double tMecanicoOcioso=0;
		
		double tFinReparacion=tInicioReparacion + calcularValRand(randomRepar[0],yRepar);
		double tFinReparacionAnt=0;
		System.out.println("T. Descompostura|Inicio T Reparaci�n|Fin T Reparacion|T Espera M�quina|T ocioso");
		System.out.println(tDescompostura+"          "+tInicioReparacion+"          "+tFinReparacion+"          "+tEsperaMaquina+"          "+tMecanicoOcioso);
		
		for(int i=0;i<20;i++) {
			tDescompostura=tDescompostura+calcularValRand(randomDes[i]-1, yDesc);
			if(tDescompostura>tFinReparacion) {
				tInicioReparacion=tDescompostura;
			}
			else {
				tInicioReparacion=tFinReparacion;
			}
			tFinReparacionAnt=tFinReparacion;
			
			tFinReparacion= tInicioReparacion + calcularValRand(randomRepar[i]-1, yRepar);
			
			tEsperaMaquina = tInicioReparacion - tDescompostura;
			tMecanicoOcioso = tInicioReparacion - tFinReparacionAnt;
			
			System.out.println(tDescompostura+"          "+tInicioReparacion+"          "+tFinReparacion+"          "+tEsperaMaquina+"          "+tMecanicoOcioso);	
		}
		
	}

	public static double calcularValRand(int i, ArrayList<Integer> yRepar) {
		return yRepar.get(i);
	}

	public static ArrayList<Integer> tReparacion(ArrayList<Integer> x) {
		int [] array= {8,9,10,11,12,13,14,15,16,17,18};
		
		ArrayList<Integer> yAcum = trepAcum(array);
		
		ArrayList<Integer> y = tRep(array);
		
		return y;
	}

	public static ArrayList<Integer> tRep(int[] array) {
		ArrayList<Integer> list=new ArrayList<Integer>();
		
		for(int i=1;i<=100;i++) {
			if (i <=3) {
				list.add(array[0]);
			}
			else if(i<=7) {
				list.add(array[1]);
			}
			else if(i<=18) {
				list.add(array[2]);
			}
			else if(i<=40) {
				list.add(array[3]);
			}
			else if(i<=59) {
				list.add(array[4]);
			}
			else if(i<=75) {
				list.add(array[5]);
			}
			else if(i<=86) {
				list.add(array[6]);
			}
			else if(i<=93) {
				list.add(array[7]);
			}
			else if(i<=97) {
				list.add(array[8]);
			}
			else if(i<=99) {
				list.add(array[9]);
			}
			else {
				list.add(array[10]);
			}
		}
		return list;
	}

	public static ArrayList<Integer> trepAcum(int[] array) {
ArrayList<Integer> list=new ArrayList<Integer>();
		
		for(int i=1;i<=100;i++) {
			if (i <=3) {
				list.add(array[0]);
			}
			else if(i<=7) {
				int sum=0;
				for(int j = 0; j < array.length-10; j++)
				    sum += array[j];
				list.add(sum);
			}
			else if(i<=18) {
				int sum=0;
				for(int j = 0; j < array.length-9; j++)
				    sum += array[j];
				list.add(sum);
			}
			else if(i<=40) {
				int sum=0;
				for(int j = 0; j < array.length-8; j++)
				    sum += array[j];
				list.add(sum);
			}
			else if(i<=59) {
				int sum=0;
				for(int j = 0; j < array.length-7; j++)
				    sum += array[j];
				list.add(sum);
			}
			else if(i<=75) {
				int sum=0;
				for(int j = 0; j < array.length-6; j++)
				    sum += array[j];
				list.add(sum);
			}
			else if(i<=86) {
				int sum=0;
				for(int j = 0; j < array.length-5; j++)
				    sum += array[j];
				list.add(sum);
			}
			else if(i<=93) {
				int sum=0;
				for(int j = 0; j < array.length-4; j++)
				    sum += array[j];
				list.add(sum);
			}
			else if(i<=97) {
				int sum=0;
				for(int j = 0; j < array.length-3; j++)
				    sum += array[j];
				list.add(sum);
			}
			else if(i<=99) {
				int sum=0;
				for(int j = 0; j < array.length-2; j++)
				    sum += array[j];
				list.add(sum);
			}
			else {
				int sum=0;
				for(int j = 0; j < array.length-1; j++)
				    sum += array[j];
				list.add(sum);
			}
		}
		return list;
	}

	public static ArrayList<Integer> tDescompuesto(ArrayList<Integer> x) {
		int [] array= {10,11,12,13,14,15,16,17,18,19};
		
		ArrayList<Integer> yAcum = tDesYAcum(array);
		
		ArrayList<Integer> y = tDesY(array);
		
		return y;
	}

	private static ArrayList<Integer> tDesY(int[] array) {
		ArrayList<Integer> list=new ArrayList<Integer>();
		
		for(int i=1;i<=100;i++) {
			if (i <=5) {
				list.add(array[0]);
			}
			else if(i<=19) {
				list.add(array[1]);
			}
			else if(i<=38) {
				list.add(array[2]);
			}
			else if(i<=60) {
				list.add(array[3]);
			}
			else if(i<=77) {
				list.add(array[4]);
			}
			else if(i<=85) {
				list.add(array[5]);
			}
			else if(i<=90) {
				list.add(array[6]);
			}
			else if(i<=95) {
				list.add(array[7]);
			}
			else if(i<=99) {
				list.add(array[8]);
			}
			else if(i==100) {
				list.add(array[9]);
			}
		}
		return list;
	}

	private static ArrayList<Integer> tDesYAcum(int[] array) {
		ArrayList<Integer> list=new ArrayList<Integer>();
		
		for(int i=1;i<=100;i++) {
			if (i <=5) {
				list.add(array[0]);
			}
			else if(i<=19) {
				int sum=0;
				for(int j = 0; j < array.length-9; j++)
				    sum += array[j];
				list.add(sum);
			}
			else if(i<=38) {
				int sum=0;
				for(int j = 0; j < array.length-8; j++)
				    sum += array[j];
				list.add(sum);
			}
			else if(i<=60) {
				int sum=0;
				for(int j = 0; j < array.length-7; j++)
				    sum += array[j];
				list.add(sum);
			}
			else if(i<=77) {
				int sum=0;
				for(int j = 0; j < array.length-6; j++)
				    sum += array[j];
				list.add(sum);
			}
			else if(i<=85) {
				int sum=0;
				for(int j = 0; j < array.length-5; j++)
				    sum += array[j];
				list.add(sum);
			}
			else if(i<=90) {
				int sum=0;
				for(int j = 0; j < array.length-4; j++)
				    sum += array[j];
				list.add(sum);
			}
			else if(i<=95) {
				int sum=0;
				for(int j = 0; j < array.length-3; j++)
				    sum += array[j];
				list.add(sum);
			}
			else if(i<=99) {
				int sum=0;
				for(int j = 0; j < array.length-2; j++)
				    sum += array[j];
				list.add(sum);
			}
			else if(i==100) {
				int sum=0;
				for(int j = 0; j < array.length-1; j++)
				    sum += array[j];
				list.add(sum);
			}
		}
		return list;
	}
	
	

}
