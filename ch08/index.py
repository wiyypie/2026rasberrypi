from flask import Flask, render_template, jsonify
import model.dht11 as db_model
import sensor.dht11 as sensor_dht

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/now")
def now():
    temp, hum = sensor_dht.get_now()

    if temp is None or hum is None:
        return jsonify({"error": "센서 읽기 실패"}), 500

    db_model.insert(hum, temp)

    result = {
        "temperature": temp,
        "humidity": hum
    }

    return jsonify(result)

@app.route("/api/record")
def record():
    result = db_model.select()
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
