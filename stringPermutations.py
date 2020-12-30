# Original problem here https://www.interviewcake.com/question/python3/recursive-string-permutations?course=fc1&section=dynamic-programming-recursion
# Write a recursive function for generating all permutations of an input string. Return them as a set.

#import unittest


def get_permutations(string):
    permus = set()
    # handle edge cases
    if len(string) == 0 or len(string) == 1:
        return set(string)
    # base case
    if len(string) == 2:
        return set(string)
    # Generate all permutations of the input string

    return set(string)

# Tests

""" class Test(unittest.TestCase):

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
        self.assertEqual(actual, expected) """


#unittest.main(verbosity=2)