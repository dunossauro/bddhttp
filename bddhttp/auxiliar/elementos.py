from os import getcwd
from os.path import join

class Constantes(object):
    """docstring for Constantes"""
    def __init__(self):
        self.local = getcwd()
        self.config = join(self.local, 'bddhttp', 'data', 'config.json')
