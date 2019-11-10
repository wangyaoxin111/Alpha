import pymssql
import traceback
from time import sleep


class PYSQL(object):


    def __init__(self, host1, server1,port1,user1, password1, database1):
        self.conn = pymssql.connect(host=host1, server=server1,port=port1,user=user1, password=password1, database=database1)
        self.cursor = self.conn.cursor()

    def create_table_func(self,sql):
        self.cursor.execute(sql)
        print('数据表创建完毕')

    def insert_date(self,sql):
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except:
            print(traceback.format_exc())
            self.conn.rollback()

    def update_data(self,sql):
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except:
            print(traceback.format_exc())
            self.conn.rollback()

    def delete_data(self,sql):
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except:
            print(traceback.format_exc())
            self.conn.rollback()

    def select_data(self, sql):
        self.cursor.execute(sql)

        all_data = self.cursor.fetchall()
        return all_data




if __name__ == '__main__':
    username="1"
    my = PYSQL('127.0.0.1','DLAPTOP-KKDTKF2S\SQLEXPRESS','49897', 'sa', '123456', 'pickme')
    data1=my.select_data('SELECT * FROM driver where dusername={}'.format(username))
    tur=data1[0]
    print(tur[2])

