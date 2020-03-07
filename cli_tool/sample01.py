# -*- coding: utf-8 -*-
from rest_client import RestClient

class Sample01():

    def __init__(self):
        pass

    def get_msg(self):
        msg = u"Hello sample01"
        return msg

    def get_value(self, a, b):
        ret = a + b
        return ret

    def get_rest_data(self, num):
        client = RestClient()
        data = client.getData(num)

        return data

    def start(self, num):

        text = self.get_msg()
        print(text)

        value = self.get_value(1, 2)
        print(value)

        try:
            data = self.get_rest_data(num)
        except Exception as e:
            print(e.message)
            return
        else:
            print(data)



