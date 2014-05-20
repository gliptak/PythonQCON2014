__author__ = 'andriod'

import Quandl


class QuandleAsset(object):
    def __init__(self, quandle_name, authtoken=None):
        """Uses the Quandl service to get live data

        :type quandle_name: str - an asset name assigned by Quandl
        :type authtoken: builtins.NoneType - Quandl auth token if available
        """
        super().__init__()
        self.value = Quandl.get(quandle_name, authtoken=authtoken)

    def __getattr__(self, item):
        """Redirect any unknown attribute access to the data retrieved from Quandl, this constitutes a complete proxy
        """
        return getattr(self.value, item)


if __name__ == "__main__":
    test = QuandleAsset("GOOG/NYSE_ERO")
    print(test)
    print(test.value)
    print(test.Close['2009-05-14'])
