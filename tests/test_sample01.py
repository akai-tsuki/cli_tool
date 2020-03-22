import unittest
from cli_tool.sample01 import Sample01
from unittest.mock import Mock


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

    def test_get_data(self):
        """ test method for get_data
        """

        # prepare
        sample = Sample01()
        expected = "bbb"

        # execute
        actual = sample.get_rest_data(1)

        # check
        self.assertEqual(expected, actual)

    def test_start(self):
        """ test method for start """

        # prepare
        sample = Sample01()
        sample.get_msg = Mock(return_value="test return msg")
        expected = True

        # execute
        actual = sample.start(1)

        # check
        sample.get_msg.assert_called()
        self.assertEqual(expected, actual)

    def test_start_error(self):
        """ test method for start """

        # prepare
        sample = Sample01()
        sample.get_msg = Mock(return_value="test return msg")
        expected = False

        # execute
        actual = sample.start(3)

        # check
        sample.get_msg.assert_called()
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
