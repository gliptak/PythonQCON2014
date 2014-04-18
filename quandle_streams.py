__author__ = 'andriod'

import Quandl

class QuandleAsset(object):
    def __init__(self, quandle_name, authtoken=None):
        super().__init__()
        self.myData = Quandl.get(quandle_name,authtoken=authtoken)

    def __getattr__(self, item):
        return getattr(self.myData,item)

    @property
    def value(self):
        return self.myData

if __name__ == "__main__":
    test = QuandleAsset("GOOG/NYSE_ERO")
    print(test)
    print(test.value)
    print(test.Close['2009-05-14'])
