import pymysql

def connect():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="q1w2e3",
        database="study",
        cursorclass=pymysql.cursors.DictCursor
    )

def insert(humidity, temperature):
    conn = connect()

    with conn.cursor() as cursor:
        sql = "INSERT INTO record_dht (humidity, temperature) VALUES (%s, %s)"
        cursor.execute(sql, (humidity, temperature))

    conn.commit()
    conn.close()

def select():
    conn = connect()

    with conn.cursor() as cursor:
        sql = """
        SELECT id, humidity, temperature,
               DATE_FORMAT(created_at, '%Y-%m-%d %H:%i:%s') AS created_at
        FROM record_dht
        ORDER BY id DESC
        """
        cursor.execute(sql)
        result = cursor.fetchall()

    conn.close()
    return result
