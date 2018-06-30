public class rotationpoint{
	public static int rotationpoint(String [] a){
		if(a.length==0){
			return 0;
		}
		else if (a.length==1){
			return 1;
		}
		// else if(a.length)
		int low=0;
		int high=a.length;
		while(low<=high){
			int mid=(low+high)/2;
			// System.out.println(mid);
			if(a[mid].charAt(0)<a[mid+1].charAt(0)&&a[mid].charAt(0)<a[mid-1].charAt(0)){
				return mid;
			}
			low=mid+1;
			if(mid+1==high){
				return high;
			}
		}
		return -1;
	}
	public static void main(String[] args) {
		String [] array = 
		{"ptolemaic", "retrograde", "supplant","undulate", "xenoepist", "asymptote",
                                      "babka", "banoffee", "engender",
                                      "karpatka", "othellolagkage"};
		System.out.println(array[rotationpoint(array)]);
	}
}