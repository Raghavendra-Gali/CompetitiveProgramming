def countMaxConsecutivesOnes(st):
	mx=0
	for i in range(len(st)-1):
		c=0
		for j in range(len(st)-1):
			if st[j] and st[j+1] =="1":
				c+=1
		if c>mx:
			mx=c
		# print(c)
	return mx


n=int(input())


print(countMaxConsecutivesOnes("{0:b}".format(n)))