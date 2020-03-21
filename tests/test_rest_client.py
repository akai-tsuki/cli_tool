import unittest
from cli_tool.rest_client import RestClient


class TestRestClient(unittest.TestCase):
    """test class of RestClient
    """

    def test_get_weather(self):
        """test method for get_msg
        """

        # prepare
        expected = 200

        # execute
        client = RestClient()
        actual = client.get_weather('140010')

        # check
        self.assertEqual(expected, actual)
