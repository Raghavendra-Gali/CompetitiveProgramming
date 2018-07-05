import unittest


def is_palindrome(s):
	return s[0::] == s[::-1]
def make_palindrome_permutation(p,s):
    print(p,s)
	n= len(s)
	if n==0:
		return is_palindrome(p)
	else:
		for i in range(n):
			if make_palindrome_permutation(p+s[i],s[0:i]+s[i+1:n]):
				return True

def has_palindrome_permutation(s):
    return make_palindrome_permutation("",s)



# Tests

class Test(unittest.TestCase):

    def test_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcbcd')
        self.assertTrue(result)

    def test_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabccbdd')
        self.assertTrue(result)

    def test_no_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcd')
        self.assertFalse(result)

    def test_no_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabbcd')
        self.assertFalse(result)

    def test_empty_string(self):
        result = has_palindrome_permutation('')
        self.assertTrue(result)

    def test_one_character_string(self):
        result = has_palindrome_permutation('a')
        self.assertTrue(result)


unittest.main(verbosity=2)