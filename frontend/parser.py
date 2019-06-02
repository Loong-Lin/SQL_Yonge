# -*- coding: utf-8 -*-
# version: Python3.6X
# Created by Lin Yonge by 2019/5

import ply.yacc as yacc
from frontend.nodes import *
from frontend import lexer

# from nodes import *
# import lexer
# Get the token map.
tokens = lexer.tokens

precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('nonassoc', 'LE', 'LE', 'GE', 'GT', 'EQ', 'NE'),  # Nonassociative operators
)


def p_start(p):
    """ start : command ';' """
    p[0] = p[1]


def p_command(p):
    """ command : ddl
                | dml
                | utility
                | nothing """
    p[0] = p[1]


def p_ddl(p):
    """ ddl : createtable
            | createindex
            | droptable
            | dropindex
            | showtables
            | altertable
            | createuser
            | grantuser
            | revokeuser """
    p[0] = p[1]


def p_dml(p):
    """ dml : query
            | insert
            | delete
            | update """
    p[0] = p[1]


def p_utility(p):
    """ utility : exit
                | print
                | desc """
    p[0] = p[1]


# 输出全部的表名
def p_showtables(p):
    """ showtables : SHOW TABLES """
    p[0] = ShowTables()


# 创建用户
def p_createuser(p):
    """ createuser : CREATE USER ID PASSWORD STRING"""
    p[0] = CreateUserNode(p[3], p[5])


# 授予用户权限
def p_grantuser(p):
    """ grantuser : GRANT power_list ON non_mrelation_list TO non_mrelation_list """
    p[0] = GrantUserNode(p[2], p[4], p[6])


# 撤销用户权限
def p_revokeuser(p):
    """ revokeuser : REVOKE power_list ON non_mrelation_list FROM non_mrelation_list """
    p[0] = RevokeUserNode(p[2], p[4], p[6])


def p_power_list(p):
    """ power_list : power_list ',' power_type
                   | power_type """
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]


def p_power_type(p):
    """  power_type : SELECT
                    | UPDATE
                    | INSERT
                    | DELETE
                    | PRINT
                    | ALL
                    | DESC
    """
    # p[0] = upper(p[1])
    p[0] = p[1].upper()


# 修改表的属性
def p_altertable(p):
    """ altertable : ALTER TABLE ID ADD attrtype
                   | ALTER TABLE ID DROP non_mrelation_list """
    p4 = p[4].upper()
    if p4 == 'ADD':
        p[0] = AlterNode(p[3], 'ADD', p[5])
    else:
        p[0] = AlterNode(p[3], 'DROP', p[5])


# 创建表
def p_createtable(p):
    """ createtable : CREATE TABLE ID '(' non_mattrtype_list ')' """
    p[0] = CreateTableNode(p[3], p[5])


# 创建表索引
def p_createindex(p):
    """ createindex : CREATE INDEX ID '(' ID ')' """
    p[0] = CreateIndexNode(p[3], p[5])


# 删除表
def p_droptable(p):
    """ droptable : DROP TABLE ID """
    p[0] = DropTableNode(p[3])


# 删除索引
def p_dropindex(p):
    """ dropindex : DROP INDEX ID '(' ID ')' """
    p[0] = DropIndexNode(p[3], p[5])


# 用print直接输出表
def p_print(p):
    """ print : PRINT ID """
    p[0] = PrintTable(p[2])


# desc，用于输出列表属性
def p_desc(p):
    """desc : DESC ID """
    p[0] = DescTable(p[2])


def p_exit(p):
    """ exit : EXIT """
    p[0] = Exit()


# 查询部分
def p_query(p):
    """ query : SELECT non_mselect_clause FROM non_mrelation_list opwhere_clause """
    p[0] = QueryNode(p[2], p[4], p[5])


# 插入值，不可有属性缺省
def p_insert(p):
    """ insert : INSERT INTO ID VALUES inservalue_list """
    p[0] = InsertNode(p[3], p[5])


# 可以缺省的方式插入
def p_inservalue_list(p):
    """ inservalue_list : '(' non_mvalue_list ')' ',' inservalue_list
                        | '(' non_mvalue_list ')' """
    if len(p) > 4:
        p[0] = [p[2]] + p[5]
    else:
        p[0] = [p[2]]


# 清空表
def p_delete(p):
    """ delete : DELETE FROM ID opwhere_clause """
    p[0] = DeleteNode(p[3], p[4])


# 更新表，即在对表中的值进行修改后的更新
def p_update(p):
    """ update : UPDATE ID SET relattr EQ relattr_or_value opwhere_clause """
    p[0] = UpdateNode(p[2], (p[4], p[6]), p[7])


def p_non_mattrtype_list(p):
    """ non_mattrtype_list : attrtype ',' non_mattrtype_list
                           | attrtype """
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]


def p_attrtype(p):
    """ attrtype : ID type
                 | ID type '(' NUMBER ')'
                 | PRIMARY KEY '(' ID ')' """
    if len(p) == 3:
        p[0] = AttrType(p[1], p[2])
    elif p[1].upper() == "PRIMARY":
        p[0] = AttrType(p[4], 'PK')
    else:
        p[0] = AttrType(p[1], p[2], p[4])


def p_type(p):
    """ type : INT
             | CHAR """
    # p[0] = upper(p[1])
    p[0] = p[1].upper()


def p_non_mselect_clause(p):
    """ non_mselect_clause : non_mrelattr_list
                           | '*' """
    p[0] = p[1]


def p_non_mrelattr_list(p):
    """ non_mrelattr_list : relattr ',' non_mrelattr_list
                          | relattr """
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]


def p_relattr(p):
    """ relattr : ID '.' ID
                | ID """
    if len(p) == 2:
        p[0] = RelAttr(p[1])
    else:
        p[0] = RelAttr(p[3], p[1])


def p_non_mrelation_list(p):
    """ non_mrelation_list : relation ',' non_mrelation_list
                           | relation """
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]


def p_relation(p):
    """ relation : ID """
    p[0] = p[1]


def p_opwhere_clause(p):
    """ opwhere_clause : WHERE non_mcond_list
                       | nothing """
    if len(p) == 3:
        p[0] = p[2]


def p_non_mcond_list(p):
    """ non_mcond_list : non_mcond_list AND non_mcond_list
                       | non_mcond_list OR  non_mcond_list
                       | '(' non_mcond_list ')'
                       | condition """
    if len(p) == 2:
        p[0] = p[1]
    elif p[1] == '(':
        p[0] = p[2]
    else:
        p[0] = Cond(p[1], p[2], p[3])


def p_condition(p):
    """ condition : relattr op relattr_or_value
                  | relattr EQ null_value
                  | relattr NE null_value """
    p[0] = Cond(p[1], p[2], p[3])


def p_relattr_or_value(p):
    """ relattr_or_value : relattr
                         | value """
    p[0] = p[1]


def p_non_mvalue_list(p):
    """ non_mvalue_list : value ',' non_mvalue_list
                        | value
                        | null_value ',' non_mvalue_list
                        | null_value """
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]


def p_value_string(p):
    """ value : STRING """
    p[0] = Value('STRING', p[1])


def p_value_number(p):
    """ value : NUMBER """
    p[0] = Value('NUMBER', p[1])


def p_null_value(p):
    """ null_value : NULL """
    p[0] = Value('NULL', None)


# 转成相应的动作
def p_op(p):
    """ op : LT
           | LE
           | GT
           | GE
           | EQ
           | NE """
    p[0] = p[1]


def p_nothing(p):
    """ nothing : """
    p[0] = None


# Error rule for syntax errors
def p_error(p):
    if not p:
        print("Syntax error, missing something (maybe ';').")
    else:
        print("Syntax error at token '%s'(%s)" % (p.value, p.type))


# Build the parser
from frontend.lexer import lexer as lex

# from lexer import lexer as lex

parser = yacc.yacc()

if __name__ == '__main__':
    while True:
        try:
            # s = raw_input('Parser > ')
            data = input("Parser>")
            while ';' not in data:
                data += input()
        except EOFError:
            break
        if not data:
            continue
        try:
            result = parser.parse(data, lexer=lex)
            print("result: ", result)
        except Exception as e:
            print(e)
