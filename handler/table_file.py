# -*- coding: utf-8 -*-
# version: Python3.6X
# Created by Lin Yonge by 2019/5

# import os
import csv
from config.config import TABLES_PATH, EXTEND_CSV

VISIBLE = False


class TableFile:
    def __init__(self, data_dict, table_name, insert_list=None):
        if insert_list is None:
            insert_list = list()
        self.attrs = [attr for attr in data_dict.dict[table_name] if attr.attr_type != "PK"]
        self.key = [attr.attr_name for attr in data_dict.dict[table_name] if attr.attr_type == "PK"]
        self.table_name = table_name
        self.file_path = TABLES_PATH + table_name + EXTEND_CSV
        self.insert_list = insert_list
        self.data_list = []

    def load_data(self):
        # file_name = TABLES_PATH + self.table_name + ".csv"
        f = open(self.file_path, "r")
        csv_reader = csv.reader(f)
        headline = next(csv_reader)
        print("headline: ", headline) if VISIBLE is True else None
        for row in csv_reader:
            print("row: ", row) if VISIBLE is True else None
            for i in range(len(self.attrs)):
                if self.attrs[i].attr_type == "INT" and row[i] != "NULL":
                    row[i] = int(row[i])
            self.data_list.append(row)
        f.close()
        return self.data_list

    def init_table(self):
        f = open(self.file_path, "w", encoding="utf-8", newline="")
        attr_name_list = [attr.attr_name for attr in self.attrs]
        headline = ",".join(attr_name_list)
        f.write(headline + "\n")

    def write_back(self):
        # file_name = TABLES_PATH + self.table_name + ".csv"
        f = open(self.file_path, "w", encoding="utf-8", newline="")
        # csv_writer = csv.writer(f)
        attr_name_list = [attr.attr_name for attr in self.attrs]
        headline = ",".join(attr_name_list)
        # csv_writer.writerow(attr_name_list)
        f.write(headline + "\n")
        for line in self.data_list:
            # line = [str(word) for word in line]
            line = ",".join([str(word) for word in line])
            f.write(line + "\n")
            # csv_writer.writerow(line)
        f.close()

    def insert(self, index_dict=None):
        # file_name = TABLES_PATH + self.table_name + ".csv"
        f = open(self.file_path, 'a', encoding="utf-8", newline="")
        csv_f = csv.writer(f)
        if not self.__check_type or not self.__check_key() and self.__check_index(index_dict):
            return False

        for value_list in self.insert_list:
            line = [value.value for value in value_list]
            csv_f.writerow(line)
        f.close()
        return True

    def __check_index(self, attr_dict):
        # 该表名没有创建过索引
        if self.table_name not in attr_dict.index_dict.keys():
            return True
        for index_name, index in attr_dict.index_dict[self.table_name].items():
            for line in self.insert_list:
                if index.has(line[index.pos].value):
                    return False
        return True

    # 如果表中已经存在相同的键，则返回False
    def __check_key(self):
        # table_data = self.load_data()
        if len(self.key) == 0:
            return True
        # file_name = TABLES_PATH + self.table_name + ".csv"
        f = open(self.file_path, "r")
        dict_csv = csv.DictReader(f)
        pk_value = []
        index_key = []
        # 获取候选键所在的列表位置
        for i in range(len(self.attrs)):
            if self.attrs[i].attr_name in self.key:
                index_key.append(i)
            elif len(index_key) == len(self.key):
                break
        # 得到候选键
        for value_list in self.insert_list:
            key = ""
            values = [value.value for value in value_list]
            print("values: ", values) if VISIBLE is True else None
            for index in index_key:
                key += str(values[index])
            pk_value.append(key)
        print("pk_value", pk_value)
        # 与表中的数据进行比较，如果有与key相同的，则返回False
        for item in dict_csv:
            value = ""
            for k in self.key:
                value += item.get(k)
            print(value, pk_value) if VISIBLE is True else None
            if value in pk_value:
                print("Error: Key error. There existed same key.")
                return False
        f.close()
        return True

    @property
    def __check_type(self):
        """
        检查插入的类型是否合法，如果合法，则返回True
        :return: bool
        """
        for val_list in self.insert_list:
            if len(val_list) != len(self.attrs):
                print("Error: Lengths are not matched.")
                return False

            for i in range(len(val_list)):  # 进行属性类型和长度检查
                if not TableFile.__is_type_match(val_list[i], self.attrs[i]):
                    print("Error: Type and value are not matched.")
                    return False
        return True

    @staticmethod
    def __is_type_match(val, attr):
        """
        检查插入的类型是否匹配
        :param val: 值
        :param attr: 属性
        :return: bool
        """
        # print("val.value_type", val, val.value_type, type(val))
        if val.value_type == "NUMBER" and attr.attr_type == "INT":
            return True
        elif val.value_type == "STRING" and attr.attr_type == "CHAR" and len(val.value) <= attr.type_len:
            return True
        elif val.value_type == "NULL":
            return True
        else:
            return False


if __name__ == "__main__":
    from handler.data_dict import DataDict
    data = DataDict("stu")
    table = TableFile(data, 'stu')
    data = table.load_data()
    for it in data:
        print(it)
    # table.write_back()
