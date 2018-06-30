import java.util.*;
public class find_in_ordered_set{
	public static boolean binarySearch(int [] a,int num){
		int low=0;
		int high=a.length;
		while(low<=high){
			int mid=(low+high)/2;
			if(a[mid]==num){
				return true;
			}
			else if (a[mid]>num){
				low=mid+1;
			}
			else{
				high=mid-1;
			}
		}
		return false;
	}
	public static void main(String[] args) {
		int [] a={1,2,3,4,5,6,7,8};
		System.out.println(binarySearch(a,8));
	}
}