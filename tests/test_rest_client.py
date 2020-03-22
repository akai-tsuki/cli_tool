import unittest
from cli_tool.rest_client import RestClient
from cli_tool.rest_client_exception import RestClientException
from unittest.mock import Mock, patch


# requests lib の mock
def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code
            self.url = "mocked_url"
            self.text = "mocked_text"

        def json(self):
            return self.json_data

    if args[0] == "http://localhost:18080/greeting":
        return MockResponse({"id": 1, "content": "Hello test name!"}, 200)
    elif args[0] == "http://weather.livedoor.com/forecast/webservice/json/v1":
        return MockResponse({}, 200)
    else:
        return MockResponse({}, 404)


class TestRestClient(unittest.TestCase):
    """test class of RestClient
    """

    def test_get_data(self):
        """ test method for get_data
        """

        # prepare
        expected = "aaa"
        # execute
        client = RestClient()
        actual = client.get_data(0)

        # check
        self.assertEqual(expected, actual)

    def test_get_data_error(self):
        """ test method for get_data in case of error.
        """

        # prepare
        client = RestClient()

        # execute
        # check
        with self.assertRaises(RestClientException):
            client.get_data(4)

    @patch("cli_tool.rest_client.requests")
    def test_get_weather(self, mock_requests):
        """test method for get_weather
        """

        # prepare
        mock_response = Mock(status_code=201, url="test_url", text="test_text")
        mock_requests.get.return_value = mock_response

        expected = 201

        # execute
        client = RestClient()
        actual = client.get_weather('140010')

        # check
        self.assertEqual(expected, actual)

    @patch('requests.get', side_effect=mocked_requests_get)
    def test_get_weather2(self, mock_requests_get):
        """test method for get_weather2
        """

        # prepare
        expected = 200

        # execute
        client = RestClient()
        actual = client.get_weather('140010')

        # check
        self.assertEqual(expected, actual)

    @patch('requests.get', side_effect=mocked_requests_get)
    def test_get_greeting(self, mock_requests_get):
        """test method for get_greeting
        """

        # prepare
        expected = "Hello test name!"

        # execute
        client = RestClient()
        actual = client.get_greeting("test name")

        # check
        self.assertEqual(expected, actual)
