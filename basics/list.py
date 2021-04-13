import re
import subprocess

class AttrTest(object):
    __weight = 50
    def __init__(self):
        super(AttrTest, self).__init__()

    @property
    def weight(self):
        return self.__weight

a = AttrTest()

print(a.weight)
a.weight = 29
print(a.weight)
