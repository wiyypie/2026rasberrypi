import pymysql
class LED:
    def __init__(self):
        self.conn=pymysql.connect(host='localhost',user='root',password='q1w2e3',db='study')
        self.cur=self.conn.cursor()
        print("connect ok!")
    
    def get(self):
        query="select * from record_led"
        self.cur.execute(query)
        result=self.cur.fetchall()
        print(result)
        return result
    def save(self,status):
        query="insert into record_led(status) values('{}')".format(status)
        self.cur.execute(query)
        self.conn.commit()

