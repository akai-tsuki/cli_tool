# -*- coding: utf-8 -*-
from cli_tool.rest_client_exception import RestClientException
import logging


class RestClient():
    """ Rest Client Sample """

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def getData(self, num):
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
