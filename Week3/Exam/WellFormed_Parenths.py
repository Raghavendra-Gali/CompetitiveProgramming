check_WellBalancedString = []


def is_valid(code):

    # Determine if the input code is valid
    stack=[]
    for i in range(len(code)):
        if code[i]=="(":
            stack.append(code[i])
        elif code[i]==")":
            if len(stack)>0:
                check = ((code[i] == ")" and stack[len(stack)-1]=="(" ))
                if check:
                    stack.pop()
                else:
                    return False
            else:
                return False
    if len(stack)==0:
        return True
    return False


def make_combination(p,s,count):
	# print(p,s)
	n= len(s)
	if n==0:
		# print(count)
		if is_valid(p) and p not in check_WellBalancedString:
			check_WellBalancedString.append(p)
	else:
		for i in range(n):
			count+=1
			make_combination(p+s[i],s[0:i]+s[i+1:n],count)

def has_combination(s):
    return make_combination("",s,0)


if __name__=='__main__':
	n = 6
	has_combination(n*"()")
	print(check_WellBalancedString,"-",len(check_WellBalancedString))

