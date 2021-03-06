import unittest
def String_in_place(message,initial,final):
	# print(message[initial:final])
	# print(initial,final)
	while initial<final:
		temp = message[initial]
		message[initial] = message[final]
		message[final] = temp
		initial+=1
		final-=1

def reverse_words(message):
    # Decode the message by reversing the words
    String_in_place(message,0,len(message)-1)
    final = True
    count=0
    for i in range(len(message)):
    	if message[i] == ' ':
    		final=False
    		String_in_place(message,count,i-1)
    		count=i+1
    if final:
    	String_in_place(message,0,len(message)-1)
    	return 
    if count<len(message)-1:
    	String_in_place(message,count,len(message)-1)


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

print(reverse_words(list('thief cake')))