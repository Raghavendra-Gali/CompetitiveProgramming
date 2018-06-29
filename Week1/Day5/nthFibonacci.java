public class nthFibonacci{
	public static int fib(int n){
		if(n==1){
			return 0;
		}
		if(n==2){
			return 1;
		}
		if(n==3){
			return 1;
		}
		int i=1;
		int j=1;
		int k=0;
		for(int r=2;r<n;r++){
			k=i+j;
			i=j;
			j=k;
		}
		return k;
	}
	public static void main(String[] args) {
		System.out.println(fib(4));
	}
}