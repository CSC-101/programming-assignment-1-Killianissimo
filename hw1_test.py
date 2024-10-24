import data
import hw1
import unittest
import math


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_vowel_count_1(self):
        input = "hello world!"
        result = hw1.vowel_count(input)
        expected = 3
        self.assertEqual(expected, result)
    def test_vowel_count_2(self):
        input = "EKOPWKJQKNX@(1023"
        result = hw1.vowel_count(input)
        expected = 2
        self.assertEqual(expected, result)

    # Part 2
    def test_short_lists_1(self):
        input = [[1,2,3],[3,4]]
        result = hw1.short_lists(input)
        expected = [[3,4]]
        self.assertEqual(expected, result)
    def test_short_lists_2(self):
        input = [[],[9]]
        result = hw1.short_lists(input)
        expected = []
        self.assertEqual(expected, result)

    # Part 3
    def test_ascending_pairs_1(self):
        input = [[1,2,3],[4,3]]
        result = hw1.ascending_pairs(input)
        expected = [[1,2,3], [3,4]]
        self.assertEqual(expected, result)
    def test_ascending_pairs_2(self):
        input = [[],[9,-10]]
        result = hw1.ascending_pairs(input)
        expected = [[], [-10,9]]
        self.assertEqual(expected, result)

    # Part 4
    def test_add_prices_1(self):
        input1 = data.Price(8, 99)
        input2 = data.Price(3, 52)
        result = hw1.add_prices(input1, input2)
        expected = data.Price(12, 51)
        self.assertEqual(expected, result)
    def test_add_prices_2(self):
        input1 = data.Price(0, 55)
        input2 = data.Price(4, 0)
        result = hw1.add_prices(input1, input2)
        expected = data.Price(4,55)
        self.assertEqual(expected, result)

    # Part 5
    def test_rectangle_area_1(self):
        input = data.Rectangle(data.Point(0,4), data.Point(5,0))
        result = hw1.rectangle_area(input)
        expected = 20
        self.assertEqual(expected, result)
    def test_rectangle_area_2(self):
        input = data.Rectangle(data.Point(4,5),data.Point(7,2))
        result = hw1.rectangle_area(input)
        expected = 9
        self.assertEqual(expected, result)

    # Part 6
    def test_books_by_author_1(self):
        inputAuthor = "John"
        inputBooks = [data.Book(["John"], "The Great Gasby"),
        data.Book(["Dave"], "1000 Leagues Under the Sea")]
        result = hw1.books_by_author(inputAuthor, inputBooks)
        expected = [data.Book(["John"], "The Great Gasby")]
        self.assertEqual(expected, result)
    def test_books_by_author_2(self):
        inputAuthor = "Bill"
        inputBooks = [data.Book(["John", "Dave", "Bill"], "Harry Potter"),
                      data.Book(["Frank", "Killian", "bill"], "The Man With the"
                                                              "Golden Gun")]
        result = hw1.books_by_author(inputAuthor, inputBooks)
        expected = [data.Book(["John", "Dave", "Bill"], "Harry Potter")]
        self.assertEqual(expected, result)

    # Part 7
    def test_circle_bound_1(self):
        input = data.Rectangle(data.Point(-2,2), data.Point(2,-2))
        result = hw1.circle_bound(input)
        expected = data.Circle(data.Point(0,0), math.sqrt(8))
        self.assertEqual(expected, result)
    def test_circle_bound_2(self):
        input = data.Rectangle(data.Point(4,5),data.Point(7,2))
        result = hw1.circle_bound(input)
        expected = data.Circle(data.Point(5.5,3.5), 2.12132034356)
        self.assertEqual(expected, result)

    # Part 8
    def test_below_average_pay_1(self):
        input = [data.Employee("John", 45),
                 data.Employee("Jeff", 85),
                 data.Employee("Britany", 55)]
        result = hw1.below_average_pay(input)
        expected = [data.Employee("John", 45),
                    data.Employee("Britany", 55)]
        self.assertEqual(expected, result)
    def test_below_average_pay_2(self):
        input = []
        result = hw1.below_average_pay(input)
        expected = "No list was provided."
        self.assertEqual(expected, result)






if __name__ == '__main__':
    unittest.main()
