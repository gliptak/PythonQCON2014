from core import Env
from dingus import Dingus
from simple_files import FileHolder

__author__ = 'andriod'




def get_dummy(env):
    return Dingus("{env_name}_env".format(env_name=env))

def get_file(env):
    return FileHolder(env)

class StoredEnv(Env):
    pass


def get_stored(env):
    return StoredEnv(env)


if __name__ == "__main__":
    print(repr(get_dummy("test")))

    print(repr(get_file("market1")))
    print(repr(get_file("market1").news))
    print(repr(get_file("market1").news['IBM']))
    print(repr(get_file("market1").news['IBM']['5-14-2010']))