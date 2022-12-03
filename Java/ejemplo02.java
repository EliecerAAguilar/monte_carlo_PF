import java.util.ArrayList;

public class ejemplo2 {

	public static void main(String[] args) {
		ArrayList<Integer> x= new ArrayList<Integer>();
		
		for(int i=0;i<100;i++) {
			x.add(i);
		}
		
		int[] vals= new int[6];
		
		for(int i=0;i<6;i++) {
			vals[i]=i;
		}
		
		int[] inter= {4,14,29,59,84,99};
		
		ArrayList<Integer> y=setY(vals,inter);
		
		montecarlo(x,y);

	}
	
	public static ArrayList<Integer> setY(int [] vals, int [] inter) {
		ArrayList<Integer> lista = new ArrayList<Integer>(); 
		int interIndex=0;
		for(int i=0;i<100;i++) {
			if(i<=inter[interIndex]) {
				
			}
			else {
				System.out.println(i);
				interIndex+=1;
			}
			lista.add(vals[interIndex]);
		}
		
		return lista;
	}
	
	public static void montecarlo(ArrayList<Integer> x,ArrayList<Integer> y) {
		int [] randNums= {14, 74, 24, 87, 7, 45, 26, 66, 26, 94};
		System.out.println("D�a  ||  Demanda");
		for(int i=1;i<11;i++) {
			
			System.out.println(i+"  ||  "+getY(randNums[i-1],y));
		}
	}
	
	public static int getY(int num, ArrayList<Integer> y) {
		return y.get(num);
	}

	}


