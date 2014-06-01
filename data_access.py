from dingus import Dingus
from quandl_streams import QuandlAsset
from simple_files import FileHolder

__author__ = 'andriod'


def get_dummy(coll_name):
    return Dingus("{coll_name}_env".format(coll_name=coll_name))


def get_file(coll_name):
    return FileHolder(coll_name)


def get_live(coll_name, sys_coll=None):
    if coll_name == 'market2':
        coll = FileHolder('market1')
        coll.etf.usd_eur = QuandlAsset("GOOG/NYSE_ERO")
        coll.fx.usd_jpy = QuandlAsset("QUANDL/USDJPY")
    elif coll_name == 'market3' and sys_coll is not None:
        coll = FileHolder('market1')
        for name, code in sys_coll.quandlFXCodes.items():
            asset = QuandlAsset(code)
            coll.fx[name] = asset

    return coll


if __name__ == "__main__":
    print(repr(get_dummy("test")))

    dummyCollection = get_dummy("market1")
    print(repr(dummyCollection))
    print(repr(dummyCollection.news))
    print(repr(dummyCollection.news['IBM']))
    print(repr(dummyCollection.news['IBM']['5-14-2010']))

    print(repr(dummyCollection.fx.usd_eur['High (est)']['2010-05-14']))
    print(repr(dummyCollection.fx.usd_eur['Low (est)']['2010-05-14']))
    print(repr(dummyCollection.fx.usd_eur.Rate['2010-05-14']))


    fileCollection = get_file("market1")
    print(repr(fileCollection))
    print(repr(fileCollection.news))
    print(repr(fileCollection.news['IBM']))
    print(repr(fileCollection.news['IBM']['5-14-2010']))

    liveCollection = get_live("market2")
    print(repr(liveCollection.fx.usd_eur['High (est)']['2010-05-14']))
    print(repr(liveCollection.fx.usd_eur['Low (est)']['2010-05-14']))
    print(repr(liveCollection.fx.usd_eur.Rate['2010-05-14']))
