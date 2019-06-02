# -*- coding: utf-8 -*-
# version: Python3.6X
# Created by Lin Yonge by 2019/5

# from frontend.lexer import lexer as lex
# from frontend.parser import parser

create_table_test = """
create table A (
  id int,
  name char(10),
  age int,
  grade int
);
"""

create_table_test2 = """
create table stu2 (
 name char(12),
 id char(8),
 sex char(4),
 primary key(id));"""

insert_test2 = "insert into stu values ('LJJ', '20164399', 'male');"

insert_test3 = 'insert into course_score values ("LJJ", "OS", 1002, 89);'

insert_test4 = 'insert into teacher values ("JinHu", "10080", "OS", 1002);'

insert_test = "insert into A1 values(5, 'c', 33, 24), (6, 'd', 33, 11);"

delete_test = "delete from A where id = 1;"

update_test = "update A set age = 1 where id = 2;"

update_test2 = "update course_score set id = '20164567' where name = 'Xuheng';"

print_test = "print A;"

alert_add_test = "alter table A add num char(20);"

alert_drop_test = "alter table A drop num;"

drop_table_test = "drop table mumu;"

select_test = "select stu.name, course_score.score from stu, course_score where stu.id = course_score.id;"

# select * from stu, course_score where stu.name = course_score.name;

create_user_test = "CREATE USER LJJ password '123';"

grant_user_test = "grant insert, delete on stu to LJJ;"

# grant insert, update on stu to Lin;

revoke_test = "revoke delete on stu from LJJ;"

'''
create table course_score (
name char(16),
course_name char(16),
cour_id int,
score int,
primary key(cour_id),
primary key(name));
'''

"""
def test_big():
    f = open("test.txt", 'w')
    for i in range(10000):
        f.write(str(i) + " " + str(i) + "\n")
    f.close()

def exec_sql(sql):
    res = parser.parse(sql, lexer=lex)
    from execute.main import execute_main
    execute_main(res)
"""


# select * from stu where stu.id = "20164399";

# select * from stu, teacher, course_score where stu.name = course_score.name and teacher.name = course_score.name;
# select * from stu, teacher where stu.name = "LJJ" and teacher.name = "JinHu"
