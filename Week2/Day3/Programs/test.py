import unittest
def String_in_place(message,initial,mid,final):
	r=final
	# print(message[initial:mid])
	for j in range(initial,mid):
		temp = message[r]
		message[r] = message[j]
		message[j] = temp 
		r-=1
	print(message)

def reverse_words(message):
    # Decode the message by reversing the words
    k=len(message)//2
    if k%2==0:
        k-=1
    c=0
    i=0
    for i in range(len(message)):
    	if message[i] == ' ':
    		r=i-1
    		md = (c+(i+1))//2
    		if md%2==0:
    			md-=1
    		String_in_place(message,c,md,i-1)
    		c=i+1
    	elif i==len(message)-1:
    		r=c
    		md = (c+len(message))//2
    		if md%2==0:
    			md-=1
    		String_in_place(message,c,md,i)
    print(i)
    String_in_place(message,0,k,i)
    return message


class Test(unittest.TestCase):

    def test_one_word(self):
        message = list('vault')
        reverse_words(message)
        expected = list('vault')
        self.assertEqual(message, expected)

    def test_two_words(self):
        message = list('thief cake')
        reverse_words(message)
        expected = list('cake thief')
        self.assertEqual(message, expected)

    def test_three_words(self):
        message = list('one another get')
        reverse_words(message)
        expected = list('get another one')
        self.assertEqual(message, expected)

    def test_multiple_words_same_length(self):
        message = list('rat the ate cat the')
        reverse_words(message)
        expected = list('the cat ate the rat')
        self.assertEqual(message, expected)

    def test_multiple_words_different_lengths(self):
        message = list('yummy is cake bundt chocolate')
        reverse_words(message)
        expected = list('chocolate bundt cake is yummy')
        self.assertEqual(message, expected)

    def test_empty_string(self):
        message = list('')
        reverse_words(message)
        expected = list('')
        self.assertEqual(message, expected)


unittest.main(verbosity=2)