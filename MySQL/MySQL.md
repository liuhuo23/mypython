# 1.SQL 语句命令
SQL 是一种数据库查询和程序设计语言
# 2. SQL 分类

1.  数据操作 dml 对数据进行 增加，修改，删除 : insert, update, delete
2. 数据定义 ddl语句 进行数据库，表的管理等 create, drop, alter,truncate
3. 事务操作tcl 语句  事务处理语言，对事物进行处理 commit, rollback, svaepoint
4. 数据控制dcl 语句 进行授权与权限回收 grand revoke

# 3. 常用命令

```sql
# 查看版本
select version()
# 显示当前时间
select now()
# 查看 所有数据库
show databases;
# 切换使用的数据库
use 数据库名
# 查看当前使用的数据库
select database();

创建数据库
create database xxx;

# 查看数据库下的表
show tables from 数据库名

# 查看表的信息
desc 表名;

# 删除数据库
drop database 数据库名

```

# 4 数据类型

``` 
# 小整数 8位
tinyint[(m)] [unsigned] [zerofill]

# 整数 32位
int[(m)] [unsigned] [zerofill]

# 大整数 64位
bigint[(m)] [unsigned] [zerofill]

# M总长 D 小数位数
FLOAT/DOUBLE[(M,D)] [unsigned] [zerofill]

# 日期类型
YERA
YYYY (1901/2155)
DATE
	YYYY-MM-DD(1000-01-01/9999-12-31)
TIME
	HH:MM:SS(-838:59:59/838:59:59)
DATETIME
	YYYY-MM-DD HH:MM:SS

TIMESTAMP
	 YYYYMMDD HHMMSS（1970-01-01 00:00:00/2037 年某时）
==注意===
# 单独插入时间 用字符串
# 插入年份 使用4位数
# 《=69 20XX年 》=70 19XX

# M总数，D小数
DECIMAL(M,D)  # 金融行业一般使用它来表示金钱
CHAR() 表示固定长度的字符串，也就是收char(4) 就是4个字节
varchar() 表示可编程的字符串，VARCHAR(4) 最大4个
TEXT 存储大文本


```

# 5 数据库中表的操作

```mysql
# 创建数据库
create database 数据库名
```

## 创建表

```mysql
CRATE TABLE 表名(
	字段名称 类型(长度) [not null] [unsigned] [zerofill] [default 值],
    PRIMARY KEY(字段名)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

