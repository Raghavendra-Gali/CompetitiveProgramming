import unittest

def max_duffel_bag_value(cake_tuples, capacity):
    for weight, value in cake_tuples:
        if weight == 0 and value > 0:
            return float('inf')
    capacity_to_value_map = [0] * (capacity + 1)
    for cap in range(0, capacity + 1):
        possible_values = [0]
        for weight, value in cake_tuples:
            if weight <= cap:
                prev_cap = cap - weight
                prev_val = capacity_to_value_map[prev_cap]
                new_val = prev_val + value
                possible_values.append(new_val)
        max_value = max(possible_values)
        if max_value == 0:
            if cap > 0:
                max_value = capacity_to_value_map[cap - 1]
        capacity_to_value_map[cap] = max_value
    return capacity_to_value_map[capacity]
# Tests

class Test(unittest.TestCase):

    def test_one_cake(self):
        actual = max_duffel_bag_value([(2, 1)], 9)
        expected = 4
        self.assertEqual(actual, expected)

    def test_two_cakes(self):
        actual = max_duffel_bag_value([(4, 4), (5, 5)], 9)
        expected = 9
        self.assertEqual(actual, expected)

    def test_only_take_less_valuable_cake(self):
        actual = max_duffel_bag_value([(4, 4), (5, 5)], 12)
        expected = 12
        self.assertEqual(actual, expected)

    def test_lots_of_cakes(self):
        actual = max_duffel_bag_value([(2, 3), (3, 6), (5, 1), (6, 1), (7, 1), (8, 1)], 7)
        expected = 12
        self.assertEqual(actual, expected)

    def test_value_to_weight_ratio_is_not_optimal(self):
        actual = max_duffel_bag_value([(51, 52), (50, 50)], 100)
        expected = 100
        self.assertEqual(actual, expected)

    def test_zero_capacity(self):
        actual = max_duffel_bag_value([(1, 2)], 0)
        expected = 0
        self.assertEqual(actual, expected)

    def test_cake_with_zero_value_and_weight(self):
        actual = max_duffel_bag_value([(0, 0), (2, 1)], 7)
        expected = 3
        self.assertEqual(actual, expected)

    def test_cake_with_non_zero_value_and_zero_weight(self):
        actual = max_duffel_bag_value([(0, 5)], 5)
        expected = float('inf')
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)