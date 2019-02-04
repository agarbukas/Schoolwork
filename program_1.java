import java.util.*;

public class program_1 {


	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner input = new Scanner(System.in);//establish scanner
		
		double [] arr = new double[5]; // new array with 5 inputs
		
		
		for(int i = 0; i < arr.length;i++) {//loop to fill the array
			
			System.out.print("Enter number " +i);//prompt
			
			arr[i] = input.nextDouble();//putting input into array
			
		
			
		}
		
		
		System.out.println("Maximum number is: " +arrayMax(arr));//maximum method call
		
		System.out.println("Minimum number is: " +arrayMin(arr));//minimum method call
		
		
		System.out.print("Augmented array");
		
		for(int indicator = 0;indicator<arr.length;indicator++) {
			
			System.out.print(arrayten(arr, indicator)+ " ");
		}
		
		
		
	
		
		
		
		
	}

	private static double arrayten(double[] arr,int indicator) {
		
		arr[indicator] += 10;
		
		return arr[indicator];
		
		
		
	
		
	}

	private static double arrayMin(double[] arr) {
		
		double min = arr[0];
		
		for(int i = 0;i < arr.length; i++) {
			
			if(arr[i] < min) {
				
				min = arr[i];
				
			}
		}
		return min;
		
	}

	private static double arrayMax(double [] arr) {
		// TODO Auto-generated method stub
		double max = arr[0];
		
		for(int i = 0; i < arr.length; i++) {
			
			if(arr[i] > max) {
				max = arr[i];
				
			}
			
		}
		
		
		return max;
	}

	
	
	
	
}
