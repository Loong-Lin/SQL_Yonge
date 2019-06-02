# -*- coding: utf-8 -*-
# version: Python3.6X
# Created by Lin Yonge by 2019/5

import time
import os

from handler.data_dict import DataDict
from frontend.nodes import NodeType
from handler.table_file import TableFile
from handler.user_dict import UserDict
from index.index_dict import IndexDict
import query
from config.config import *
from frontend.parser import parser
from frontend.lexer import lexer

index_dict = IndexDict(INDEX_PATH)
user_dict = UserDict(USER_PATH)
VISIBLE = False


# 创建表
def execute_create_table(node):
    if not __check_power(node.type, [node.table_name]):
        return
    # 如果该表已经存在，则返回None
    if __check_table([node.table_name]):
        print("Error: This table already exists.")
        return

    data_dict = DataDict(node.table_name)
    data_dict.dict[node.table_name] = node.attr_list
    data_dict.write_back()
    table = TableFile(data_dict, node.table_name)
    table.init_table()
    # user_dict.create_table(node.table_name)


def execute_insert(node):
    if not __check_power(node.type, [node.table_name]):
        return
    if not __check_table([node.table_name]):
        print("Error: This table isn't exists.")
        return
    data_dict = DataDict(node.table_name)
    table = TableFile(data_dict, node.table_name, node.value_list)
    print("node.table_name: ", node.table_name)
    if not table.insert(index_dict):
        print("Error: Types are not matched or Key error or index duplicated")
        return
    index_dict.load_index()  # 加载索引


def execute_print_table(node):
    if not __check_power(node.type, [node.table_name]):
        return
    if not __check_table([node.table_name]):
        print("Error: This table isn't exists.")
        return
    data_dict = DataDict(node.table_name)
    names = data_dict.table_attr_names()
    data = TableFile(data_dict, node.table_name).load_data()
    print_table(names, data)


def execute_delete(node):
    if not __check_power(node.type, [node.table_name]):
        return
    if not __check_table([node.table_name]):
        print("Error: This table isn't exists.")
        return
    data_dict = DataDict(node.table_name)
    names = data_dict.table_attr_names()
    table = TableFile(data_dict, node.table_name)
    table_data = table.load_data()
    old_len = len(table_data)
    print("where_list: ", node.where_list, type(node.where_list))
    # for where_item in node.where_list:
    #     print("where_item", where_item)
    try:
        table.data_list = []
        for line in table_data:
            is_true = check_where(node.where_list, names, line)
            print("is_true: ", is_true) if VISIBLE is True else None
            if not is_true:
                table.data_list.append(line)
    except Exception as ex:
        print("Error: %s." % ex)
        return
    new_len = len(table.data_list)
    table.write_back()
    index_dict.load_index()  # 表中记录删除后，索引文件也要相应的发生改变
    print("%d line(s) are deleted." % (old_len - new_len))


def execute_drop_table(node):
    if not __check_power(node.type, [node.table_name]):
        return
    if not __check_table([node.table_name]):
        print("Error: This table isn't exists.")
        return

    file_name = TABLES_PATH + node.table_name + ".csv"
    dict_name = DATA_DICT_PATH + node.table_name + ".csv"
    os.remove(file_name)  # remove table file
    os.remove(dict_name)  # remove data_dict file
    index_dict.drop_table(node.table_name)  # 索引文件也要同步drop
    print('OK. Drop table %r successful.' % node.table_name)


def execute_alert(node):
    if not __check_power(node.type, [node.table_name]):
        return
    if not __check_table([node.table_name]):
        print("Error: This table isn't exists.")
        return
    data_dict = DataDict(node.table_name)
    names = data_dict.table_attr_names()
    table = TableFile(data_dict, node.table_name)
    table_data = table.load_data()
    if node.op == "ADD":
        if node.attr_list.attr_name in names:
            print("Error: The attr's name already exists.")
            return
        data_dict.dict[node.table_name] += [node.attr_list]
        for line in table_data:
            line.append("NULL")
        # for idx in range(len(table_data)): table_data[idx].append("NULL")
    elif node.op == "DROP":
        attr_name = node.attr_list[0]
        # for it in node.attr_list:
        #     print(it, type(it))
        if attr_name not in names:
            print("Error: The attr's name does not exist.")
            return
        old_list = data_dict.dict[node.table_name]
        data_dict.dict[node.table_name] = [attr for attr in old_list if attr.attr_name != attr_name]
        index_remove = names.index(attr_name)
        for line in table_data:
            line.pop(index_remove)
        # 当某个属性drop是，如果其有索引，则也要相应的drop
        index_dict.drop_index(node.table_name, attr_name)
    # print("table.data_list: ")
    # for it in table.data_list:
    #     print(it)
    # table.data_list = table_data
    table.write_back()
    data_dict.write_back()
    print("Alert table successful.")


def execute_update(node):
    if not __check_power(node.type, [node.table_name]):
        return
    if not __check_table([node.table_name]):
        print("Error: This table isn't exists.")
        return
    data_dict = DataDict(node.table_name)
    names = data_dict.table_attr_names()
    table = TableFile(data_dict, node.table_name)
    table_data = table.load_data()
    update_line = 0
    try:
        for line in table_data:
            # 如果line符合where的条件，则返回True
            if check_where(node.where_list, names, line):
                set_value(line, names, node.set_list)
                print("node.where_list: ", node.where_list)
                update_line += 1
    except Exception as ex:
        print("Error: %s." % ex)
        return
    table.write_back()
    index_dict.load_index()  # 表中记录更新后，索引文件也要相应的发生改变
    print("%d line(s) are updated." % update_line)


def execute_select(node):
    if not __check_power(node.type, node.from_list):
        return
    if not __check_table(node.from_list):
        print("Error: This table isn't exists.")
        return
    __dur()
    print("\n" + "node.select_list: ") if VISIBLE is True else None
    for it in node.select_list:
        print(it, end=", ") if VISIBLE is True else None
    print("\n" + "node.from_list: ") if VISIBLE is True else None
    for it in node.from_list:
        print(it, end=", ") if VISIBLE is True else None
    print("\n" + "node.where_list: ")  # if VISIBLE is True else None
    print(node.where_list)  # if VISIBLE is True else None
    part_name = []  # 只存属性名
    full_name = []  # 表名和属性名都存，格式: [table_name.attr_name1, table_name.attr_name2,...]
    # table_data = []
    table_datas = dict()  # 表的数据
    for table_name in node.from_list:
        data_dict = DataDict(table_name)
        names = data_dict.table_attr_names()
        part_name += names
        full_name += [table_name + '.' + attr_name for attr_name in names]
        # table_data += [TableFile(data_dict, table_name).load_data()]

    name_dict = {}
    for idx in range(len(full_name)):
        name_dict[full_name[idx]] = idx
        name_dict[part_name[idx]] = idx

    if node.select_list[0] == "*":
        node.select_list = full_name
    try:
        # 先进行选择
        if len(node.from_list) >= 2 and node.where_list:
            node_value = __get_where_value([node.where_list])
            if len(node_value) > 0:
                for it in node_value:
                    # print("node.left.attr_name: ", it.left.table_name)
                    table_name = str(it.left.table_name)
                    table_datas[table_name] = []
                    data_dict = DataDict(table_name)
                    names = data_dict.table_attr_names()
                    data = TableFile(data_dict, table_name).load_data()
                    for line in data:
                        if check_where(it, names, line):
                            table_datas[table_name].append(line)

        for it in node.from_list:
            if it in table_datas.keys():
                continue
            data_dict = DataDict(it)
            data = TableFile(data_dict, it).load_data()
            table_datas[it] = data
            # print("data: ", data)

        table_data = list(table_datas.values())
        # print("table_data; ", table_data)
        # 找出要投影属性的位置
        select_col_nums = [name_dict[str(attr_name)] for attr_name in node.select_list]
        # 判断是否可以用索引来做连接，两个表的
        if node.where_list and len(node.from_list) == 2 and \
                __can_use_index_joint(node.from_list[0], node.where_list):
            print("This query used index 1.")
            res = query.joint_by_index(table_data, node.from_list[0],
                                       node.where_list.left.attr_name, index_dict)
            if len(res) == 0:
                res = query.joint(table_data)
        else:
            # 直接做笛卡尔积，返回做完笛卡尔积的结果
            res = query.joint(table_data)

        # 判断是否可以利用索引来做选择，对于第一个表
        if node.where_list and __can_use_index_select(node.from_list[0], node.where_list):
            print("This query used index 2.")
            val = node.where_list.right.value
            num = index_dict.query(node.from_list[0], node.where_list.left.attr_name, [val])[0]
            res = [res[num]] if num is not None else []

        selected_data = []
        for line in res:

            # print(node.where_list, "\n", part_name, "\n", line, "\n", full_name)
            if check_where(node.where_list, part_name, line, full_name):
                selected_data.append(line)
        projection_data = query.projection(selected_data, select_col_nums)
        print_table(node.select_list, projection_data)

        __dur("Select")
    # except ZeroDivisionError:
    #     print("Error.")
    except Exception as ex:
        print("Error: %s." % ex)


def execute_create_index(node):
    if not __check_power(node.type, [node.table_name]):
        return
    print("node.table_name: ", node.table_name)
    if not __check_table([node.table_name]):
        print("Error: This table isn't exists.")
        return
    data_dict = DataDict(node.table_name)
    attr_names = data_dict.table_attr_names()
    if node.attr_name not in attr_names:
        print("Error: The table_attr does not exist.")
        return
    if index_dict.has_index(node.table_name, node.attr_name):
        print("Error: The index already exist.")
        return
    data = TableFile(data_dict, node.table_name).load_data()
    index_dict.create_index(node.table_name, node.attr_name, attr_names, data)
    index_dict.write_back()


def execute_drop_index(node):
    if not __check_power(node.type, [node.table_name]):
        return
    if not __check_table([node.table_name]):
        print("Error: This table isn't exists.")
        return
    data_dict = DataDict(node.table_name)
    attr_names = data_dict.table_attr_names()
    if node.attr_name not in attr_names:
        print("Error: The table_attr does not exist.")
        return
    if not index_dict.has_index(node.table_name, node.attr_name):
        print("Error: The index does not exist.")
        return
    index_dict.drop_index(node.table_name, node.attr_name)


def execute_desc_table(node):
    if not __check_table([node.table_name]):
        print("Error: This table isn't exists.")
        return
    names = ["attr_name", "attr_type", "attr_len"]
    data_dict = DataDict(node.table_name)
    data = data_dict.dict[node.table_name]
    # for it in data:
    #     line = str(it).split(" ")
    #     print(line)
    data = [str(it).split(" ") for it in data]
    print_table(names, data)


def execute_create_user(node):
    if node.user_id in user_dict.password.keys():
        print("Error: The username already existed.")
    print("create user.")
    tables_name = get_tables()
    user_dict.create_user(node.user_id, node.password, tables_name)
    user_dict.write_back()


def execute_grant_user(node):
    user_dict.add_power(node.user_list, node.table_list, node.power_list)
    user_dict.write_back()
    print("Grant user successful!")


def execute_revoke_user(node):
    user_dict.remove_power(node.user_list, node.table_list, node.power_list)
    user_dict.write_back()
    print("Revoke user successful!")


def print_table(names, data, width=COLUMN_WIDTH):
    len_list = [int((len(str(name)) + 1) / 2) for name in names]
    for i in range(len(len_list)):
        if len_list[i] < width:
            len_list[i] = width
    table = "┌"
    n = len(names)
    for i in range(n):
        width = len_list[i]
        table += "─" * width + ("─" if i != n - 1 else "─┐\n")
    # fmt = "│%" + str(width * 2) + "s"
    for i in range(len(names)):
        width = len_list[i]
        # width = int(len(name) / 2)
        fmt = "│%" + str(width * 2) + "s"
        table += fmt % names[i]
    table += "│\n├"
    for i in range(n):
        width = len_list[i]
        table += "─" * width + ("─" if i != n - 1 else "─┤\n")
    for line in data:
        for i in range(len(line)):
            width = len_list[i]
            fmt = "│%" + str(width * 2) + "s"
            table += fmt % line[i]
        table += "│\n"
    table += "└"
    for i in range(n):
        width = len_list[i]
        table += "─" * width + ("─" if i != n - 1 else "─┘")
    print(table)


def set_value(data_line, names, set_list):
    assert len(names) == len(data_line)
    attr_dict = {}
    for key, value in zip(names, data_line):
        attr_dict[key] = value
    origin = __get_value(set_list[0], attr_dict)  # 数据记录中原来的值
    update = __get_value(set_list[1], attr_dict)  # 需要更新数据属性的新值
    print("origin, update: ", origin, update, type(origin), type(update)) if VISIBLE is True else None
    attr_index = names.index(set_list[0].attr_name)  # 获得属性所在的列表位置
    if origin != "NULL" and update != "NULL" and type(origin) != type(update):
        raise Exception("Error: Type not match!")
    data_line[attr_index] = update  # 通过更改传入的形参list来改变实参，再重新写回表中


def check_where(where_node, part_names, data_line, full_names=None):
    """
    用于判断该行是否符合条件, 如果符合条件，则返回True，否则返回False
    :param where_node: where后面的条件
    :param part_names: 表的属性
    :param data_line: 表中的一条记录
    :param full_names:
    :return:
    """
    assert len(part_names) == len(data_line)  # 如果表中的属性个数与记录的值个数不相同，则抛出异常
    if not where_node:  # 即没有where条件时，全部记录清除
        return True
    # dict = {}
    attr_dict = {}
    for idx in range(len(part_names)):
        attr_dict[part_names[idx]] = data_line[idx]
    if full_names:
        for idx in range(len(full_names)):
            attr_dict[full_names[idx]] = data_line[idx]
    print("attr_dict: ", attr_dict) if VISIBLE is True else None
    return __check_node(where_node, attr_dict)


def get_tables():
    tables = os.listdir(TABLES_PATH)
    table_names = []
    for it in tables:
        name = it.split(".")[0]
        table_names.append(name)
    print(table_names)
    return table_names


# 检查是否存在相同的表，如果已存在，则返回True; 否则返回False
def __check_table(table_list):
    filename = TABLES_PATH + '{}' + EXTEND_CSV
    dict_filename = DATA_DICT_PATH + '{}' + EXTEND_CSV
    for table in table_list:
        file_path = filename.format(table)
        dict_file_path = dict_filename.format(table)
        print(file_path, dict_file_path) if VISIBLE is True else None
        # f1 = os.path.exists(file_path)
        # f2 = os.path.exists(dict_file_path)
        # print(f1, f2)
        if not os.path.exists(file_path) or not os.path.exists(dict_file_path):
            # print("FileNotFoundError, file %r isn't Exist." % (table + EXTEND_CSV))
            return False
    return True


def __dur(op=None, clock=[time.time()]):
    # if clock is None:
    #     clock = [time.time()]
    if op:
        duration = time.time() - clock[0]
        print('%s finished. Duration %.6f seconds.' % (op, duration))
    clock[0] = time.time()


def __get_value(node, attr_dict):
    print("node, ", node, node.type) if VISIBLE is True else None
    # eg: name,type(name) is RELATTR = NodeType.relation_attr
    if node.type == NodeType.relation_attr:
        # print("node, node.attr_name", node, node.attr_name)
        value = attr_dict.get(str(node))
        if value is None:
            value = attr_dict.get(str(node.attr_name), None)
        return value
    else:  # eg: LJJ[STRING]，返回LJJ
        print("node, node.value: ", node, node.value) if VISIBLE is True else None
        return node.value


# 获得where后面的值，用来做选择
def __get_where_value(node_list):
    print("node: ", node_list[0]) if VISIBLE is True else None
    assert (node_list[0].type == NodeType.condition)
    node_value = []
    for node in node_list:
        if node.op == "AND":  # 递归比较
            return __get_where_value([node.left, node.right])
        elif node.op == "OR":
            return __get_where_value([node.left, node.right])
        elif node.op != "AND" and node.op != "OR":
            # node_value = []
            if node.left.type == NodeType.relation_attr and node.right.type == NodeType.value:
                node_value.append(node)
    return node_value


def __check_node(node, attr_dict):
    """
    用于条件比较, 相当于将字符串转换成比较符
    :param node: (attr_name, value, op), eg: (name, LJJ[STRING], =)
    :param attr_dict: {attr_name1: value1, attr_name2: value2, ...}
    :return: bool
    """
    print("node: ", node) if VISIBLE is True else None
    assert (node.type == NodeType.condition)
    if node.op == "AND":  # 递归比较
        return __check_node(node.left, attr_dict) and __check_node(node.right, attr_dict)
    elif node.op == "OR":
        return __check_node(node.left, attr_dict) or __check_node(node.right, attr_dict)
    elif node.op == ">=":
        return __get_value(node.left, attr_dict) >= __get_value(node.right, attr_dict)
    elif node.op == "<=":
        return __get_value(node.left, attr_dict) <= __get_value(node.right, attr_dict)
    elif node.op == ">":
        return __get_value(node.left, attr_dict) > __get_value(node.right, attr_dict)
    elif node.op == "<":
        return __get_value(node.left, attr_dict) < __get_value(node.right, attr_dict)
    elif node.op == "=":
        print("node.left: ", node.left, "node.right: ", node.right) if VISIBLE is True else None
        return __get_value(node.left, attr_dict) == __get_value(node.right, attr_dict)
    elif node.op == "!=":
        return __get_value(node.left, attr_dict) != __get_value(node.right, attr_dict)


def __can_use_index_select(table_name, where_node):
    # 左边是属性名，右边为值，操作符为 "=", 属性名有索引
    # is_has_index = index_dict.has_index(table_name, where_node.left.attr_name)
    # print("is_has_index:", is_has_index)
    if where_node.left.type == NodeType.relation_attr and where_node.right.type == NodeType.value \
            and where_node.op == "=" and index_dict.has_index(table_name, where_node.left.attr_name):
        return True
    else:
        return False


def __can_use_index_joint(table_name, where_node):
    # is_has_index = index_dict.has_index(table_name, where_node.left.attr_name)
    if where_node.left.type == NodeType.relation_attr and where_node.right.type == NodeType.relation_attr \
            and where_node.op == "=" and index_dict.has_index(table_name, where_node.left.attr_name):
        return True
    else:
        return False


def __check_power(node_type, table_list):
    if user_dict.has_power(table_list, [node_type]):
        return True
    else:
        print("Error: The user does not have this permission.")
        return False


def execute_main(command):
    # print("command.type: ", command.type, type(command.type), type(NodeType.create_table))
    if command.type == NodeType.create_table:
        execute_create_table(command)
    elif command.type == NodeType.insert:
        execute_insert(command)
    elif command.type == NodeType.print_table:
        execute_print_table(command)
    elif command.type == NodeType.drop_table:
        execute_drop_table(command)
    elif command.type == NodeType.alter:
        execute_alert(command)
    elif command.type == NodeType.delete:
        execute_delete(command)
    elif command.type == NodeType.update:
        execute_update(command)
    elif command.type == NodeType.select:
        # t0 = time.time()
        execute_select(command)
        # duration = time.time() - t0
        # print('Select finished. Duration %.6f seconds.' % duration)
    elif command.type == NodeType.show_tables:
        print("NodeType: ", NodeType.show_tables)
        # execute_show_tables(command)
    elif command.type == NodeType.create_index:
        execute_create_index(command)
    elif command.type == NodeType.drop_index:
        execute_drop_index(command)
    elif command.type == NodeType.desc_table:
        print(command.type)
        execute_desc_table(command)
    elif command.type == NodeType.create_user:
        execute_create_user(command)
    elif command.type == NodeType.grant_user:
        execute_grant_user(command)
    elif command.type == NodeType.revoke_user:
        execute_revoke_user(command)


def login():
    username = input('Enter username: ')
    # password = getpass.getpass('Enter password: ')
    password = input("Enter password: ")
    if user_dict.check(username, password):
        UserDict.CurrentUser = username
        user_dict.show_power(username)
        return True
    else:
        return False


# from frontend.parser import parser
# from frontend.lexer import lexer

if __name__ == "__main__":
    while not login():
        print("Password or username is not correct!")

    while True:
        command_line = input("Yonge_SQL>")
        while ';' not in command_line:
            command_line += input()
        print("command: ", command_line)
        try:
            result = parser.parse(command_line, lexer=lexer)
        except Exception as e:
            print("Error is: ", e)
        else:
            if not result:
                continue
            if result.type == "EXIT":
                break
            # print("OK, result: ", result, type(result))
            execute_main(result)
