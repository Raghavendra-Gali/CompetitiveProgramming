def convertToBinary(integer):
	st = "{0:b}".format(integer)
	print("convertToBinary",st)
	return st

def addZero(integer,n):
	# print("integer",n,integer)
	st = n*"0"
	st+=integer
	# print("addZero",st)
	return st


if __name__ == '__main__':

	a = 1
	b =  4



	c,d="",""
	c=convertToBinary(a)
	d = convertToBinary(b)
	if len(c)<len(d):
		c = addZero(c,len(d)-len(c))
	elif len(c)>len(d):
		d = addZero(d,len(c)-len(d))

	count=0
	j=0
	for i in range(len(c)):
		if c[i]!=d[j]:
			count+=1
		j+=1
	print(count)
