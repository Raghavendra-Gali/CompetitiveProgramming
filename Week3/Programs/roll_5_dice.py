import random


def rand5():
	def rand7(): return random.randint(1,7)
	res=7
	while res>5:
		res = rand7()
	return res

print("Rolling 5-sided dice")
print(rand5())