# -*- coding: utf-8 -*-
from rest_client_exception import RestClientException

class RestClient():

    def __init__(self):
        #
        pass

    def getData(self, num):
        data = ["aaa", "bbb", "ccc"]

        ret_value = "not_select"

        try:
            ret_value = data[num]
        except Exception as e:
            print(e)
            print(type(e))

            raise RestClientException('msg: %s, input: %s' % (e.message, num))

        return ret_value


