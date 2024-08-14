import os


def mkfile(_path_):
    if not os.path.exists(_path_):
        _file_ = open(_path_, 'x')
        _file_.close()