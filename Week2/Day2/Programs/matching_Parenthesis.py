import unittest


def get_closing_paren(sentence, opening_paren_index):

    # Find the position of the matching closing parenthesis
    res=0

    for i in range(opening_paren_index,len(sentence)):
        if sentence[i]=="(":
            res+=1
        if sentence[i]==")":
            res-=1
            if res==0:
                # print(i)
                return i
    if res!=0:
        raise Exception("No closing parenths")


# Tests

class Test(unittest.TestCase):

    def test_all_openers_then_closers(self):
        actual = get_closing_paren('((((()))))', 2)
        expected = 7
        self.assertEqual(actual, expected)


    def test_mixed_openers_and_closers(self):
        actual = get_closing_paren('()()((()()))', 5)
        expected = 10
        self.assertEqual(actual, expected)

    def test_no_matching_closer(self):
        with self.assertRaises(Exception):
            get_closing_paren('()(()', 2)


unittest.main(verbosity=2)