import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.Dictionary;
import java.util.Enumeration;
import java.util.Hashtable;
import java.util.Iterator;
import java.util.List;
import java.util.Random;
import java.util.Scanner;

public class ejemplo10 {

	public static void main(String[] args) {
		Scanner input = new Scanner(System. in);
		System.out.print("Cantidad de llegadas: ");
		double n=input.nextDouble();
		
		games(n);

	}
	
	public static void games(double n){
		ArrayList<String> choices= new ArrayList<String>();
		choices.add("T,T,T");
		choices.add("T,T,H");
		choices.add("T,H,T");
		choices.add("T,H,H");
		choices.add("H,T,T");
		choices.add("H,T,H");
		choices.add("H,H,T");
		choices.add("H,H,H");
		
		ArrayList<String> tableWins= new ArrayList<String>();
		
		Dictionary semiWins = new Hashtable();
		
		String choice1="";
		String choice2="";
		for(int i=0;i<8;i++) {
			choice1=choices.get(i);
			for(int j=0;j<8;j++) {
				choice2=choices.get(j);
				
				int wins=0;
				if(choice1.equals(choice2) == false) {
					
					String p1choice = choice1;
					String p2choice = choice2;
					
					for(int k=0;k<n;k++) {
						int vic=pennysgame(p1choice,p2choice);
						if(vic==1) {
							wins+=1;
						}
					semiWins.put(choice1+"/"+choice2,wins);
					}
				}
				else {
					semiWins.put(choice1+"/"+choice2,0);
				}
			}
		
		}
		
	
     
        for (Enumeration k = semiWins.keys(); k.hasMoreElements();) 
        { 	
        	String key=(String) k.nextElement();
        	int value= (int) semiWins.get(key);
        	double valueD=value;

        	System.out.print(key+"= " );
        	System.out.println(valueD/n);
        } 
		 

	  

		
		
	}

	public static int pennysgame(String p1choice, String p2choice) {
		Random r = new Random();
		ArrayList<String> coinsOptions= new ArrayList<String>();
		coinsOptions.add("T");
		coinsOptions.add("H");
		int returnValue=2;
		
		List<String> coin= new ArrayList<String>();
		
		for(int i=0;i<3;i++) {
			
			coin.add(coinsOptions.get(r.nextInt(2)));
		}
		
		boolean doo=true;
		
		while(doo==true) {
			
			List<String> al = new ArrayList<String>(Arrays.asList(p1choice.split(",")));
			
			boolean flag=false;
			
			for(int j=0;j<3;j++) {
	
				if(al.get(j).equals(coin.get(j))) {
					flag=true;
				}
				else {
					flag=false;
				}
				
			}
			
			if(flag) {
				doo=false;
				
				returnValue=1;
				
			}
			else if(flag==false) {
				doo=false;
	
				returnValue=0;
			}
			
			else {
				coin=(ArrayList<String>) coin.subList(1, coin.size()-1);
				coin.add(coinsOptions.get(r.nextInt(2)));
		
			}
		}

		return returnValue;
	}

}
