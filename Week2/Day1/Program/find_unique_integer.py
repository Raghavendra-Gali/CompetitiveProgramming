import unittest


def find_unique_delivery_id(delivery_ids):

    # Find the one unique ID in the list
    """
    v=None
    for i in range(len(delivery_ids)):
        c=0
        for j in range(len(delivery_ids)):
            if delivery_ids[i]==delivery_ids[j]:
                c+=1
        if c==1:
            v=delivery_ids[i]
    return v
    #O(n^2) solution
    """
    """Using XOR operation on an array we would get unique element present in it in O(n) complexity"""
    
    if len(delivery_ids)==1:
        return delivery_ids[0]
    res = delivery_ids[0] ^ delivery_ids[1]
    for i in range(2,len(delivery_ids)):
        res = res^delivery_ids[i]
    return res


# Tests

class Test(unittest.TestCase):

    def test_one_drone(self):
        actual = find_unique_delivery_id([1])
        expected = 1
        self.assertEqual(actual, expected)

    def test_unique_id_comes_first(self):
        actual = find_unique_delivery_id([1, 2, 2])
        expected = 1
        self.assertEqual(actual, expected)

    def test_unique_id_comes_last(self):
        actual = find_unique_delivery_id([3, 3, 2, 2, 1])
        expected = 1
        self.assertEqual(actual, expected)

    def test_unique_id_in_middle(self):
        actual = find_unique_delivery_id([3, 2, 1, 2, 3])
        expected = 1
        self.assertEqual(actual, expected)

    def test_many_drones(self):
        actual = find_unique_delivery_id([2, 5, 4, 8, 6, 3, 1, 4, 2, 3, 6, 5, 1])
        expected = 8
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)