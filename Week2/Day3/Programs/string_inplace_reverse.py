import unittest


def reverse(list_of_chars):

    # Reverse the input list of chars in place
    if len(list_of_chars)==0:
        return []
    if len(list_of_chars)==1:
        return list_of_chars
    r=len(list_of_chars)-1
    # print(len(list_of_chars)//2)
    k = len(list_of_chars)//2
    if k%2==0:
        k+=1
    # print(k)
    for i in range(k):
        temp = list_of_chars[i]
        list_of_chars[i] = list_of_chars[r]
        list_of_chars[r] = temp
        r-=1
        # print(temp,list_of_chars) 
    return list_of_chars




# Tests

class Test(unittest.TestCase):

    def test_empty_string(self):
        list_of_chars = []
        reverse(list_of_chars)
        expected = []
        self.assertEqual(list_of_chars, expected)

    def test_single_character_string(self):
        list_of_chars = ['A']
        reverse(list_of_chars)
        expected = ['A']
        self.assertEqual(list_of_chars, expected)

    def test_longer_string(self):
        list_of_chars = ['A', 'B', 'C', 'D', 'E']
        reverse(list_of_chars)
        expected = ['E', 'D', 'C', 'B', 'A']
        self.assertEqual(list_of_chars, expected)


unittest.main(verbosity=2)