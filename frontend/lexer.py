# -*- coding: utf-8 -*-
# version: Python3.6X
# Created by Lin Yonge by 2019/5

import ply.lex as lex


# List of token names.
reversed = (
    # Main
    'CREATE', 'TABLE', 'DROP', 'SHOW', 'ALTER', 'SELECT', 'FROM', 'WHERE',
    'INSERT', 'DELETE', 'UPDATE', 'VIEW', 'USER', 'REVOKE', 'GRANT',
    'INDEX', 'LOAD', 'SET', 'INTO', 'VALUES', 'TABLES', 'ADD', "ON", "TO",
    'PASSWORD', 'CREATETABLE', 'CREATEUSER', 'DROPTABLE', 'DROPINDEX', 'CREATEINDEX',
    # Modifier
    'PRIMARY', 'KEY', 'DESC', 'ASC', 'ALL',
    # Const Value
    'NULL',
    # Command
    'HELP', 'PRINT', 'EXIT',
    # Operator
    'AND', 'OR', 'IS', 'NOT',
    # Type
    'INT', 'CHAR',
)

tokens = reversed + (
    # Symbol
    'ID', 'NUMBER', 'STRING',
    # Operator
    'EQ', 'LT', 'LE', 'GT', 'GE', 'NE',
)

# Regular expression rules for simple tokens
t_EQ = r'='
t_GT = r'>'
t_GE = r'>='
t_LT = r'<'
t_LE = r'<='
t_NE = r'!='

literals = ['(', ')', ',', ';', '.', '+', '-', '*', '/']

# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'

# Ignore note
t_ignore_note = r'\/\*.*?\*/'


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = 'ID' if t.value.upper() not in reversed else t.value.upper()  # Check for reserved words
    # t.type = 'ID' if upper(t.value) not in reversed else upper(t.value)  # Check for reserved words
    return t


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_STRING(t):
    r'(\'|").*?(\'|")'
    t.value = t.value[1: -1]
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Error handling rule
def t_error(t):
    print("LexError [%s, %s]: Illegal character '%s'." % (t.lexer.lineno, t.lexer.lexpos, t.value[0]))


lexer = lex.lex()


if __name__ == '__main__':
    # data = raw_input('Lexer > ')
    # data = input("Lexer>")
    data = input("Lexer>")
    while ';' not in data:
        data += input()
    print("data: ", data)
    lexer.input(data)
    while True:
        tok = lexer.token()
        print("tok: ", tok, type(tok))
        if not tok:
            print("not token.")
            break
        # print(tok)
