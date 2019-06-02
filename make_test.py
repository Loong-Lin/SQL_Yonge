# -*- coding: utf-8 -*-
# version: Python3.6X
# Created by Lin Yonge by 2019/5

import os
from config.config import *


names = os.listdir(TABLES_PATH)
print(names)

list1 = ["a", "b", "c"]
list2 = ["e", "f", "g"]
list1 = list1 + list2
a = False
VERBOSE = True
print(list1) if a is True else None


line = "name CHAR 10\n"
line_list = line[:-1].split(" ")
print(line_list)


def get_tables():
    tables = os.listdir(TABLES_PATH)
    table_names = []
    for it in tables:
        name = it.split(".")[0]
        table_names.append(name)
    print(table_names)
    return table_names

get_tables()
