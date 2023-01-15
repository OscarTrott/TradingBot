import re

def findElemInList(list, name):
    for x in list:
        if re.match(name, x):
            return x
    return None
