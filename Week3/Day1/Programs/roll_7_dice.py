import random

def rand7():
	def rand5(): return random.randint(1,5)
	while True:
		throw_one = rand5()
		throw_two = rand5()
		total_Events = (throw_one-1)*5+(throw_two-1)+1
		if total_Events > 21:
			continue
		return total_Events%7+1

print('Rolling 7-sided dice')
print(rand7())