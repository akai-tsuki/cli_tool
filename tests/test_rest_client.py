import unittest
from cli_tool.rest_client import RestClient
from unittest.mock import Mock, patch


class TestRestClient(unittest.TestCase):
    """test class of RestClient
    """

    @patch("cli_tool.rest_client.requests")
    def test_get_weather(self, mock_requests):
        """test method for get_weather
        """

        mock_response = Mock(status_code=201, url="test_url", text="test_text")
        mock_requests.get.return_value = mock_response

        # prepare
        expected = 201

        # execute
        client = RestClient()
        actual = client.get_weather('140010')

        # check
        self.assertEqual(expected, actual)

    def test_get_greeting(self):
        """test method for get_greeting
        """

        # prepare
        expected = "Hello test name!"

        # execute
        client = RestClient()
        actual = client.get_greeting("test name")

        # check
        self.assertEqual(expected, actual)
