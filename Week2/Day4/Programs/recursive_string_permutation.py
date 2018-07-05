import unittest


strings_permutes=set()

def make_palindrome_permutation(p,s):
	n= len(s)
	if n==0:
		if p not in strings_permutes and p!='':
			strings_permutes.add(p)
	else:
		for i in range(n):
		    make_palindrome_permutation(p+s[i],s[0:i]+s[i+1:n])


def get_permutations(string):

    # Generate all permutations of the input string
    if string == '':
        return set([''])
    if len(string) == 1:
    	return set([string])
    make_palindrome_permutation("",string)
    print(strings_permutes)
    # s=set(lilst(strings_permutes))
    # strings_permutes=set()
    s=set(list(strings_permutes))
    strings_permutes.clear()
    return s



# Tests


class Test(unittest.TestCase):

    def test_empty_string(self):
        actual = get_permutations('')
        expected = set([''])
        self.assertEqual(actual, expected)

    def test_one_character_string(self):
        actual = get_permutations('a')
        expected = set(['a'])
        self.assertEqual(actual, expected)

    def test_two_character_string(self):
        actual = get_permutations('ab')
        expected = set(['ab', 'ba'])
        self.assertEqual(actual, expected)

    def test_three_character_string(self):
        actual = get_permutations('abc')
        expected = set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
