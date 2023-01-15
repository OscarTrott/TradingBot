# -*- coding: utf-8 -*-
import re


def findElemInList(list, name):
    for x in list:
        if re.match(f".*{name}.*", x):
            return x
    return None
