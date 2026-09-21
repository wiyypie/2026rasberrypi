import pymysql

import pymysql

class TodoDB:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='q1w2e3', db='study')
        self.cur = self.db.cursor()
        print("connect ok")
    def get(self):
        sql="select * from todos"
        self.cur.execute(sql)
        values= self.cur.fetchall()
        return values
    def add(self, task):
        sql = "INSERT INTO todos (task) VALUES (%s)"
        self.cur.execute(sql, (task))
        self.db.commit()
    def remove(self,todo_index):
        sql=f"delete from todos where todo_index={todo_index}"
        self.cur.execute(sql)
        self.db.commit()
