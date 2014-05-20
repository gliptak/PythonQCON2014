from dingus import Dingus
from quandle_streams import QuandleAsset
from simple_files import FileHolder

__author__ = 'andriod'


def get_dummy(coll_name):
    return Dingus("{coll_name}_env".format(coll_name=coll_name))


def get_file(coll_name):
    return FileHolder(coll_name)


def get_live(coll_name):
    env = FileHolder(coll_name)
    env.fx.usd_eur = QuandleAsset("GOOG/NYSE_ERO")
    env.fx.usd_jpy = QuandleAsset("QUANDL/USDJPY")
    return env


if __name__ == "__main__":
    print(repr(get_dummy("test")))

    fileCollection = get_file("market1")
    print(repr(fileCollection))
    print(repr(fileCollection.news))
    print(repr(fileCollection.news['IBM']))
    print(repr(fileCollection.news['IBM']['5-14-2010']))

    liveCollection = get_live("market2")
    print(repr(liveCollection.fx.usd_eur.Volume['2010-05-14']))