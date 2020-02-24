import unittest
from cli_tool.sample01 import Sample01

class TestSample01(unittest.TestCase):
    """test class of sample01.py
    """

    def test_show(self):
        """test method for show
        """

        # prepare
        expected = "Hello sample01"

        # execute
        sample = Sample01()
        actual = sample.get_msg()

        # check
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()