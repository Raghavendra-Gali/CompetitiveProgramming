import unittest


def is_single_riffle(half_one, half_two, shuffled_deck):

    half_one_index = 0
    half_two_index = 0
    half_one_max_index = len(half_one)-1
    half_two_max_index = len(half_two)-1

    if len(half_one) == len(half_two):
        return True
    if len(half_one)==0:
        return True
    for card in shuffled_deck:
        if half_one_index <= half_one_max_index and card == half_one[half_one_index]:
            half_one_index += 1
        elif half_two_index <=  half_two_max_index and card == half_two[half_one_index]:
            half_two_index += 1
        else:
            return False
    return True







# Tests

class Test(unittest.TestCase):

    def test_both_halves_are_the_same_length(self):
        result = is_single_riffle([1, 4, 5], [2, 3, 6], [1, 2, 3, 4, 5, 6])
        self.assertTrue(result)

    def test_halves_are_different_lengths(self):
        result = is_single_riffle([1, 5], [2, 3, 6], [1, 2, 6, 3, 5])
        self.assertFalse(result)

    def test_one_half_is_empty(self):
        result = is_single_riffle([], [2, 3, 6], [2, 3, 6])
        self.assertTrue(result)

    def test_shuffled_deck_is_missing_cards(self):
        result = is_single_riffle([1, 5], [2, 3, 6], [1, 6, 3, 5])
        self.assertFalse(result)

    def test_shuffled_deck_has_extra_cards(self):
        result = is_single_riffle([1, 5], [2, 3, 6], [1, 2, 3, 5, 6, 8])
        self.assertFalse(result)


unittest.main(verbosity=2)