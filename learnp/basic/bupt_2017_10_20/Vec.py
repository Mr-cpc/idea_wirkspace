import abc
class Vec:
    def __init__(self,data):
        self.data = data[:]

    @abc.abstractmethod
    def mul(self,vec):pass