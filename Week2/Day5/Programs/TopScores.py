import unittest


def sort_scores(unsorted_scores, highest_possible_score):

    # Sort the scores in O(n) time
    if len(unsorted_scores)<=1:
        return unsorted_scores
    scores = [None]*len(unsorted_scores)
    for i in range(highest_possible_score+1):
        scores.append(0)
    print(scores)
    for i in unsorted_scores:
        unsorted_scores[i]=unsortedd_scores[i]+1
    sortScores=[]

    for i in range(highest_possible_score,-1,-1):
        j = sortScores[i]
        for k in range(0,j):
            sortScores.append(i)
    return sortScores







# Tests

class Test(unittest.TestCase):

    def test_no_scores(self):
        actual = sort_scores([], 100)
        expected = []
        self.assertEqual(actual, expected)

    def test_one_score(self):
        actual = sort_scores([55], 100)
        expected = [55]
        self.assertEqual(actual, expected)

    def test_two_scores(self):
        actual = sort_scores([30, 60], 100)
        expected = [60, 30]
        self.assertEqual(actual, expected)

    def test_many_scores(self):
        actual = sort_scores([37, 89, 41, 65, 91, 53], 100)
        expected = [91, 89, 65, 53, 41, 37]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)