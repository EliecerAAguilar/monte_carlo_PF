import java.util.ArrayList; 
public class ejemplo3 {

	public static void main(String[] args) {
		ArrayList<Integer> x; 
		
		ArrayList<Integer> y;
		
		ArrayList<Integer> z;
		
		int[] vals= new int[6];
		
		for(int i=0;i<6;i++) {
			vals[i]=i;
		}
		
		int[] inter1= {9, 29, 54, 79, 94, 99};
		
		int n=99;
		
		x=setVar(vals,inter1,n);
		
		for(int i=0;i<4;i++) {
			vals[i]=i;
		}
		
		int[] inter2= {24, 54, 79, 99};
		
		y=setVar(vals,inter2,n);
		
		for(int i=0;i<3;i++) {
			vals[i]=i;
		}
		
		int[] inter3= {2,7,9};
		
		n=9;
		
		z=setVar(vals,inter3,n);
		
		funcEfectividad(x,y,z);
		

	}

	
	public static ArrayList<Integer> setVar(int [] vals,int [] inter,int n){
		ArrayList<Integer> list = new ArrayList<Integer>(); 
		int interIndex=0;
		for(int i=0;i<=n;i++) {
			if(i<=inter[interIndex]) {
				
			}
			else {
				interIndex+=1;
			}
			list.add(vals[interIndex]);
		}
		
		return list;
	}
	
	public static void funcEfectividad(ArrayList<Integer> x,ArrayList<Integer> y,ArrayList<Integer> z) {
		int [] randX = {43, 96, 57, 53, 14, 3, 33, 40};
		int [] randY = {22, 50, 13, 36, 91, 58, 45, 43};
		int [] randZ = {1, 8, 0, 2, 7, 6, 1, 3};
		int xi,yi,zi;
		double wi=0;
		System.out.println("Rand X || Val X || Rand Y || Val Y || Rand Z || Val Z || X+4Y+3Z");
		
		for(int i=0;i<8;i++) {
			xi=getVar(randX[i],x);
			yi=getVar(randY[i],y);
			zi=getVar(randZ[i],z);
			
			wi=xi+4*yi+3*zi;
			
			System.out.println(randX[i]+" || "+xi+" || "+randY[i]+" || "+yi+" || "+randZ[i]+" || "+zi+" || "+wi);
		}

	}
	
	public static int getVar(int num, ArrayList<Integer> y) {
		return y.get(num);
	}
}
