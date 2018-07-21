def CountOne(st):
	c=0
	for i in range(len(st)):
		if st[i]=="1":
			c+=1
	return c


n = int(input())

res=[]
for i in range(n+1):
	res.append(CountOne("{0:b}".format(i)))
print(res)