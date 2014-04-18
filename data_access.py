from core import Env
from dingus import Dingus
from quandle_streams import QuandleAsset
from simple_files import FileHolder

__author__ = 'andriod'




def get_dummy(env_name):
    return Dingus("{env_name}_env".format(env_name=env_name))

def get_file(env_name):
    return FileHolder(env_name)

def get_live(env_name):
    env = FileHolder(env_name)
    env.fx.usd_eur=QuandleAsset("GOOG/NYSE_ERO")
    return env

class StoredEnv(Env):
    pass


def get_stored(env_name):
    return StoredEnv(env_name)


if __name__ == "__main__":
    print(repr(get_dummy("test")))

    print(repr(get_file("market1")))
    print(repr(get_file("market1").news))
    print(repr(get_file("market1").news['IBM']))
    print(repr(get_file("market1").news['IBM']['5-14-2010']))

    print(repr(get_live("market1").fx.usd_eur.Volume['2010-05-14']))