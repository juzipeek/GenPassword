# -*- coding:utf-8 -*-

'''
简短地生成随机密码，包括大小写字母、数字，可以指定密码长度
首字母大写，其余小写
并将密码保存在Sqlite数据库
'''
import string
import sqlite3
from random import choice
from datetime import datetime

'''
建表语句:
create table password(
 password  varchar(40),
 description varchar(256),
 datetime    varchar(19)
);
insert into password(password, description, datetime) values ();
'''

# python3中为string.ascii_letters,
# 而python2下则可以使用string.letters和string.ascii_letters

## 数据库文件
DB_FILE = "d:\password.db"


def GenPassword(charlen=5, digitlen=3, chars=string.ascii_letters, digits=string.digits):
    pre = ''.join([choice(chars) for i in range(charlen)])
    post = ''.join([choice(digits) for i in range(digitlen)])
    raw = pre + post
    password = string.upper(raw[0]) + string.lower(raw[1:])
    return password


##保存密码
def SavePassword(password, desc, db=DB_FILE):
    stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    runsql = "insert into password(password, description, datetime)" \
             " values ('{0}','{1}', '{2}')".format(password, desc, stamp)
    conn = sqlite3.connect(db)
    try:
        conn.execute(runsql)
        conn.commit()
    except:
        print "Save Password Error!",
    finally:
        conn.close()


## 生成密码主函数
## desc:密码用途
def Main(desc):
    password = GenPassword()
    print("Gen {0} Password: {1}".format(desc, password))
    SavePassword(password, desc)


if __name__ == "__main__":
    Main("生成测试密码")

