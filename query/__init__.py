# -*- coding: utf-8 -*-
# version: Python3.6X
# Created by Lin Yonge by 2019/5


# 投影
def projection(table, col_num_list):
    res = []
    for line in table:
        new_line = [line[i] for i in col_num_list]
        res += [new_line]
    return res


# 连接操作，做笛卡尔积
def joint(tables):
    res = None
    for table in tables:
        if res is None:
            res = table
            continue
        temp = []
        for x in res:
            for y in table:
                temp += [x + y]
        res = temp
    return res


# 选择
def select(table, col_num_list):
    return [table[i] for i in col_num_list]


# 通过索引来做连接
def joint_by_index(tables, table_name, index_name, index_dict):
    res = []
    # print("table_name, index_name: ", table_name, index_name)
    for line in tables[1]:
        # print("line: ", line)
        x = line[0]
        num = index_dict.query(table_name, index_name, [x])[0]
        # print("num: ", num)
        if num is not None:
            res += [tables[0][num] + line]
    return res


# def can_use_index(where_list, index_dict):
#     return False
