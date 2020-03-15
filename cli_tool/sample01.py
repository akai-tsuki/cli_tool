# -*- coding: utf-8 -*-
from cli_tool.rest_client import RestClient

import logging


class Sample01():
    """ sample class for CLI Tool """

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def get_msg(self):
        msg = u"Hello sample01"
        self.logger.info("msg: " + msg)
        return msg

    def get_value(self, a, b):
        ret = a + b
        self.logger.info("value: " + str(ret))
        return ret

    def get_rest_data(self, num):
        client = RestClient()
        data = client.getData(num)

        self.logger.info("data: " + str(data))

        return data

    def start(self, num):

        self.logger.info("Start sample")

        print("name:" + __name__)

        text = self.get_msg()
        print("msg: " + text)

        value = self.get_value(1, 2)
        print("value: " + str(value))

        try:
            data = self.get_rest_data(num)
        except Exception as e:
            print("error msg: " + str(e.message))
            return
        else:
            print("output data: " + str(data))
