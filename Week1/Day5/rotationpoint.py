def findrotationpoint(array):
	if len(array)==0:
		return 
	elif len(array)==1:
		return 0
	else:
		low,high=0,len(array)-1
		while low<=high:
			mid=(low+high)//2
			if array[mid]<array[mid-1] and array[mid]<array[mid+1]:
				return mid
			low=mid+1
			if mid+1==high:
				return high
		return -1

