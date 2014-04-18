__author__ = 'andriod'


class Asset(object):
    def __init__(self, env, datatype, name):
        self.env = env
        self.datatype = datatype
        self.name = name
    def __getattr__(self, item):
        self.curve(self.env,self.datatype,self.name,item)


class Datatype(object):
    asset = Asset

    def __init__(self, env, name):
        self.env = env
        self.name = name
    def __getitem__(self, item):
        ret = self.asset(self.env, self.datatype, item)
        setattr(self,item,ret)
        return ret


class Env(object):
    datatype = Datatype
    def __getattr__(self, item):
        ret = self.datatype(self,item)
        setattr(self,item,ret)
        return ret