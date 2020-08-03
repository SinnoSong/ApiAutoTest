import os,sys

from config import setting
from pymysql import connect,cursors
from  pymysql.err import OperationalError
import configparser as cparser

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# 读取config.ini的配置文件
cf = cparser.ConfigParser()
cf.read(setting.TEST_CONFIG,encoding="utf-8")
host = cf.get("mysql_conf","host")
port = cf.get("mysql_conf","port")
user = cf.get("mysql_conf","user")
password = cf.get("mysql_conf","password")
database_message = cf.get("mysql_conf","database_message")
database_sso = cf.get("mysql_conf","database_sso")
database_store = cf.get("mysql_conf","database_store")

class DB:
    """
    MySQL基本操作
    """
    def __init__(self,database):
        try:
            # 连接数据库
            self.conn = connect(host = host,
                                user = user,
                                password = password,
                                db = database,
                                charset = 'utf8mb4',
                                cursorclass = cursors.DictCursor
                                )
        except OperationalError as e:
            print("Mysql Error %d: %s" % (e.args[0],e.args[1]))

    #查询数据
    def select(self,table_name,row_name='*',where_statements=""):
        select_sql = "select "+row_name+"from "+table_name+"where "+where_statements
        with self.conn.cursor() as cursor:
            cursor.execute(select_sql)
        self.conn.commit()

    #关闭链接
    def close(self):
        self.conn.close()