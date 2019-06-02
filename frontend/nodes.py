# -*- coding: utf-8 -*-
# version: Python3.6X
# Created by Lin Yonge by 2019/5


class NodeType:
    select = 'SELECT'
    insert = 'INSERT'
    delete = 'DELETE'
    update = 'UPDATE'
    alter = 'ALTER'
    create_table = 'CREATETABLE'
    drop_table = 'DROPTABLE'
    create_index = 'CREATEINDEX'
    drop_index = 'DROPINDEX'
    create_user = 'CREATEUSER'
    exit = 'EXIT'
    print_table = 'PRINT'
    desc_table = 'DESC'  # desc table
    show_tables = 'SHOW'
    value = 'VALUE'
    condition = 'CONDITION'
    relation_attr = 'RELATTR'
    grant_user = 'GRANTUSER'
    revoke_user = 'REVOKEUSER'
    attr_type = "ATTRTYPE"


class QueryNode:
    def __init__(self, select_list, from_list, where_list):
        self.type = NodeType.select
        self.select_list = select_list
        self.from_list = from_list
        self.where_list = where_list


class InsertNode:
    def __init__(self, table_name, value_list):
        self.type = NodeType.insert
        self.table_name = table_name
        self.value_list = value_list


class DeleteNode:
    def __init__(self, table_name, where_list):
        self.type = NodeType.delete
        self.table_name = table_name
        self.where_list = where_list


class UpdateNode:
    def __init__(self, table_name, set_list, where_list):
        self.type = NodeType.update
        self.table_name = table_name
        self.set_list = set_list
        self.where_list = where_list


class AlterNode:
    def __init__(self, table_name, op, attr_list):
        self.type = NodeType.alter
        self.table_name = table_name
        self.op = op
        self.attr_list = attr_list

    def __str__(self):
        attr_list = self.attr_list.__str__()
        return "(" + self.op + ", " + attr_list + ")"


class CreateTableNode:
    def __init__(self, table_name, attr_list):
        self.type = NodeType.create_table
        self.table_name = table_name
        self.attr_list = attr_list


class DropTableNode:
    def __init__(self, table_name):
        self.type = NodeType.drop_table
        self.table_name = table_name


class CreateIndexNode:
    def __init__(self, table_name, attr_name):
        self.type = NodeType.create_index
        self.table_name = table_name
        self.attr_name = attr_name


class DropIndexNode:
    def __init__(self, table_name, attr_name):
        self.type = NodeType.drop_index
        self.table_name = table_name
        self.attr_name = attr_name


class CreateUserNode:
    def __init__(self, user_id, password):
        self.type = NodeType.create_user
        self.user_id = user_id
        self.password = password


class GrantUserNode:
    def __init__(self, power_list, table_list, user_list):
        self.type = NodeType.grant_user
        self.power_list = power_list
        self.table_list = table_list
        self.user_list = user_list


class RevokeUserNode:
    def __init__(self, power_list, table_list, user_list):
        self.type = NodeType.revoke_user
        self.power_list = power_list
        self.table_list = table_list
        self.user_list = user_list


class Exit:
    def __init__(self):
        self.type = NodeType.exit


class PrintTable:
    def __init__(self, table_name):
        self.type = NodeType.print_table
        self.table_name = table_name


class DescTable:
    def __init__(self, table_name):
        self.type = NodeType.desc_table
        self.table_name = table_name


class ShowTables:
    def __init__(self):
        self.type = NodeType.show_tables


class Value:
    def __init__(self, value_type, value):
        self.type = NodeType.value
        self.value_type = value_type
        self.value = value

    def __str__(self):
        return str(self.value) + '[' + self.value_type + ']'


class RelAttr:
    def __init__(self, attr_name, table_name=None):
        self.type = NodeType.relation_attr
        self.table_name = table_name
        self.attr_name = attr_name

    def __str__(self):
        if self.table_name:
            return self.table_name + '.' + self.attr_name
        else:
            return self.attr_name


# 用于where后面的条件提取, 格式为: 属性名，属性值，操作符
class Cond:
    def __init__(self, left, op, right):
        self.type = NodeType.condition
        self.op = op.upper()
        # self.op = upper(op)
        self.left = left
        self.right = right

    def __str__(self):
        return '(' + str(self.left) + ', ' + str(self.right) + ', ' + self.op + ')'


class AttrType:
    def __init__(self, attr_name, attr_type, type_len=11):
        self.type = NodeType.attr_type
        self.attr_type = attr_type
        self.type_len = int(type_len)
        self.attr_name = attr_name

    def __str__(self):
        return self.attr_name + " " + self.attr_type + " " + str(self.type_len)
