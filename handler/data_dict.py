# -*- coding: utf-8 -*-
# version: Python3.6X
# Created by Lin Yonge by 2019/5


import os
import csv
from frontend.nodes import AttrType
from config.config import *

VISIBLE = False


# 每个表都有一个字典文件
class DataDict:
    def __init__(self, table_name):
        self.dict = {}
        self.table_name = table_name
        self.file_path = DATA_DICT_PATH + table_name + EXTEND_CSV
        self.load_data()

    def load_data(self):
        print("file_path: ", self.file_path) if VISIBLE is True else None
        if not os.path.exists(self.file_path):
            # f = open(self.file_path, "w")
            return
        f = open(self.file_path, "r")
        # f.seek(0)
        csv_reader = csv.reader(f)
        # next(csv_reader)
        headline = next(csv_reader)
        print("headline: ", headline) if VISIBLE is True else None
        for row in csv_reader:
            print("row: ", row) if VISIBLE is True else None
            if not self.dict.get(self.table_name):
                self.dict[self.table_name] = [AttrType(*row)]
            else:
                self.dict[self.table_name] += [AttrType(*row)]  # 扩展字典值的列表
        f.close()

    def table_attr_names(self):
        attr_name_list = []
        # print("self.table_name: ", self.table_name)
        for attr in self.dict[self.table_name]:
            # print("attr: ", attr)
            if attr.attr_type != "PK":
                attr_name_list.append(attr.attr_name)
        return attr_name_list

    def attr_type(self):
        return self.dict[self.table_name].attr_type

    def write_back(self):
        f = open(self.file_path, "w", encoding="utf-8", newline="")
        csv_f = csv.writer(f)
        headline = ["attr_name", "attr_type", "attr_len"]
        csv_f.writerow(headline)
        values = self.dict[self.table_name]
        for it in values:
            line = str(it).split(" ")
            csv_f.writerow(line)
        f.close()


if __name__ == '__main__':
    data = DataDict("A")
    # print(data.tables_name())
    # print data.tables_name()

    # data.dict = {
    #     "A" : [AttrType("age", "INT", 0), AttrType("name", "CHAR", 10)],
    #     "B" : [AttrType("age", "INT", 0), AttrType("name", "CHAR", 10), AttrType("age", "PK", 0)]
    # }
    # data.write_back()
