meetings=[(0,1),(3,5),(4,8),(10,12),(9,10)]

def merge_ranges(x):
	meeting=[x[0]]
	for i in range(1,len(x)):
		if meeting[i-1][1]>=x[i][0]:
			

