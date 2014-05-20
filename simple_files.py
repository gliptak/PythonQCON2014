import os
import pandas
import yaml


__author__ = 'andriod'


class FileHolder(object):
    next_type = None


    def __init__(self, name, *prev_path):
        self.name = name
        self.path = prev_path + (self,)
        self.is_dir = os.path.isdir(self.file_path)

        self._cache = {}
        if self.next_type is None:
            self.next_type = type(self)

    def create_sub_obj(self, item):
        if hasattr(self,'yaml_dict'):
            return self.yaml_dict[item]
        elif os.path.isfile(self.file_path + ".yaml"):
            self.yaml_dict = yaml.load(open(self.file_path + ".yaml"))
            return self.yaml_dict[item]
        elif os.path.isfile(os.path.join(self.file_path, item) + ".csv"):
            return pandas.DataFrame.from_csv(os.path.join(self.file_path, item) + ".csv")

        return self.next_type(item, *self.path)

    @property
    def file_path(self):
        return str(os.path.join(*[x.name for x in self.path]))

    @property
    def value(self):
        if self.is_dir:
            return "Directory, no value"
        elif os.path.isfile(self.file_path):
            return open(self.file_path).read()
        elif os.path.isfile(self.file_path + ".yaml"):
            return yaml.load(open(self.file_path + ".yaml"))

    def __getitem__(self, item):
        ret = self.create_sub_obj(item)
        self._cache[item] = ret
        return ret
    def __getattr__(self, item):
        if item not in ['yaml_dict'] and not item[0] == "_":
            ret = self.create_sub_obj(item)
            setattr(self, item, ret)
            return ret
        else:
            raise AttributeError

    def __repr__(self, *args, **kwargs):
        return "< {path} - {value} ".format(path = ",".join(x.name for x in self.path), value= self.value)

    def __str__(self, *args, **kwargs):
        return str(self.value)

