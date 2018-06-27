def coinCount(amount,denomination):
	if amount==0:
		return 1
	elif amount<0:
		return 0
	if len(denomination)==0:
		return 0
	return coinCount(amount-denomination[0],denomination)+coinCount(amount,denomination[1:])

print(coinCount(4,[1,2,3]))
print(coinCount(4, [1, 2, 3]))
print(coinCount(0, (1, 2)))