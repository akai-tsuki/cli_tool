# -*- coding: utf-8 -*-
from cli_tool.rest_client_exception import RestClientException
import logging
import requests


class RestClient():
    """ Rest Client Sample """

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def get_data(self, num):
        data = ["aaa", "bbb", "ccc"]

        ret_value = "not_select"

        try:
            self.logger.debug("num: " + str(num))
            ret_value = data[num]

        except Exception as e:
            self.logger.debug(str(e))
            self.logger.debug(str(type(e)))

            raise RestClientException('msg: %s, input: %s' % (e.message, num))

        return ret_value

    def get_weather(self, id):
        url = "http://weather.livedoor.com/forecast/webservice/json/v1"

        city = {'city':  '140010'}
        response = requests.get(url, params=city)

        print("URL: " + response.url)
        print("Text: " + response.text)

        return response.status_code

    def get_greeting(self, name):
        url = "http://localhost:18080/greeting"

        name = {'name': name}
        response = requests.get(url, params=name)

        json_data = response.json()
        print(json_data)

        return json_data["content"]
