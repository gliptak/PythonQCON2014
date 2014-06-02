from copy import deepcopy
from operator import add
import re



__author__ = 'andriod'


def point_tweak(collection, curve, date, operation, amount):
    path = [x for x in re.split("[\.[\]]", curve) if x]
    collection = deepcopy(collection)
    curr = collection
    for element in path:
        curr = curr[element]
    curr[date] = operation(curr[date], amount)
    return collection


if __name__ == "__main__":
    from data_access import get_live, get_file, get_dummy

    dummyCollection = get_dummy("test")
    baseVol = dummyCollection['fx']["usd_eur"]['Volume']['2010-05-14']
    point_tweak(dummyCollection, 'fx[usd_eur].Volume', '2010-05-14', add, .001)
    tweakedVol = dummyCollection['fx']["usd_eur"]['Volume']['2010-05-14']
    print(baseVol, tweakedVol)
    print(repr(dummyCollection))

    fileCollection = get_file("market1")
    print(repr(fileCollection))
    print(repr(fileCollection.news))
    print(repr(fileCollection.news['IBM']))
    print(repr(fileCollection.news['IBM']['5-14-2010']))

    liveCollection = get_live("market2")
    print(repr(liveCollection.fx.usd_eur.Volume['2010-05-14']))