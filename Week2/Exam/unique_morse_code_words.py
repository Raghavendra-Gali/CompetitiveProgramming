def find_transformation_word(word,morse_code):
	st=""
	for i in word:
		st+=morse_code[i]
	return st


morse_code = {"A":".-",
"B":"-...",
"C" :"-.-.",
"D" :"-..",
"E" :".",
"F" :"..-.",
"G" :"--.",
"H" :"....",
"I" :"..",
"J" :".---",
"K" :"-.-",
"L" :".-..",
"M" :"--",	
"N" :"-.",
"O" :"---",
"P" :".--.",
"Q" :"--.-",
"R" :".-.",
"S" :"...",
"T" :"-",
"U" :"..-",
"V" :"...-",
"W" :".--",
"X" :"-..-",
"Y" :"-.--",
"Z" :"--.."
}

sentence = [["gin", "zen", "gig", "msg"],["a", "z", "g", "m"], ["bhi", "vsv", "sgh", "vbi"],
	    ["a", "b", "c", "d"],["hig", "sip", "pot"]]


for words in sentence:
	transformations={}
	for word in words:
		transform=find_transformation_word(word.upper(),morse_code)
		if transform not in transformations:
			transformations[transform]=1
		else:
			transformations[transform]+=1

	print(len(transformations))


# print(morse_code)
