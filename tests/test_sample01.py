import unittest
from cli_tool.sample01 import Sample01


class TestSample01(unittest.TestCase):
    """test class of sample01.py
    """

    def test_get_msg(self):
        """test method for get_msg
        """

        # prepare
        expected = "Hello sample01"

        # execute
        sample = Sample01()
        actual = sample.get_msg()

        # check
        self.assertEqual(expected, actual)

    def test_get_value(self):
        """test method for get_value
        """

        # prepare
        expected = 3

        # execute
        sample = Sample01()
        actual = sample.get_value(1, 2)

        # check
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
