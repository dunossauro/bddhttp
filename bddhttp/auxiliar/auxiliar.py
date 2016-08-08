from json import loads

def read_config(path):
    return loads(open(path).read())
