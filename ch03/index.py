from flask import Flask, render_template
import pymysql
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

#상단에 import pymysql 추가

@app.route("/<num>")
def up(num):
    print(num)
    num = int(num)
    print("받은 숫자:", num)

    # 2. pymysql로 MySQL 연결
    conn = pymysql.connect(
        host="localhost",
        user="lee",
        password="q1w2e3",
        database="study",
        port=3306,
        charset="utf8mb4"
    )

    cursor = conn.cursor()

    # 1. numcount 테이블 생성
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS numcount (
            id INT AUTO_INCREMENT PRIMARY KEY,
            num INT NOT NULL,
            insert_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # 3. 증가한 수만큼 추가
    for i in range(num):
        cursor.execute(
            "INSERT INTO numcount (num) VALUES (%s)",
            (i + 1,)
        )

    conn.commit()

    # 4. 연결 끊기
    cursor.close()
    conn.close()
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
