import sys
def checkTrueOrFalse(s,t):
	j=0
	for i in range(len(s)):
		if s[i]!=' ' or t[j]!=' ':
			if s[i]!=t[j]:
				return str(False)
		j+=1
	return str(True)

# i=1
# strings=""
# for line in sys.stdin:
# 	strings+=line
# print(strings)

# i=0
# for i in range(len(strings)-2):
# 	# print(strings[i])

# 	# # s=strings[i].strip('\n')
# 	# t=strings[i+1].strip('\n')
# 	# a=strings[i+2].strip('\n')
# 	# print(s,t)
# 	# # s = [i.lower() for i in s ]
# 	# # t = [i.lower() for i in t ]
# 	# s=s.capitalize()
# 	# t=t.capitalize()
# 	# s=list(s)
# 	# t=list(t)
# 	# s.sort()
# 	# t.sort()
# 	# print(s,t)
# 	# print(checkTrueOrFalse(s,t)==a)
s=input().strip(" ")
t=input().strip(" ")
s=s.lower()
s=s.replace(" ","")
t=t.replace(" ","")
print(s)
t=t.lower()
s=list(s)
t=list(t)
print(s,t)
s.sort()
t.sort()
print(checkTrueOrFalse(s,t))	





# test_cases = strings.split(",")
# print(test_cases)

# for test_case in test_cases:
# 	s = test_case.strip(" \n")
	# t = strip(" \n")
	# a = line.strip(" \n")
	# a=a.capitalize()
	# s = [i.lower() for i in s if i!=' ']
	# t = [i.lower() for i in t if i!=' ']
	# s.sort()
	# t.sort()
	# print(checkTrueOrFalse(s,t)==a)



