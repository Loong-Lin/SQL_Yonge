#DBMS base on Python 3.6
DBMS (Database Management Sysytem)
##The DBMS using PLY to paser.
   这是我的一个课程的实验，我在编译部分基本上都是借用tiraffe的SQLolita的编译，但在文件结构上
我做了优化，采用csv文件进行存储，使读取更加便捷。在数据字典文件方面，
我也有自己的想法，既然table都是一个文件放一个table，那每个table的
数据字典也应该是一个文件存放一个data dict。\
   在查询方面，我也做了优化，按照启发式查询树的方式进行优化，把选择
提前做，投影也提前做。但还没有全部完成，还会继续优化。

##reference:
[1] https://github.com/tiraffe/SQLolita\
[2] https://www.kancloud.cn/kancloud/ply\
[3]
