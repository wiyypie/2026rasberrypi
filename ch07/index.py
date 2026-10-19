from flask import Flask, request, render_template, jsonify
import RPi.GPIO as GPIO
from time import sleep

app = Flask(__name__)

SERVO_PIN = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)

servo = GPIO.PWM(SERVO_PIN, 50)
servo.start(0)


def setAngle(angle):
    duty = 2.5 + 10 * angle / 180
    servo.ChangeDutyCycle(duty)
    sleep(0.5)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/angle', methods=['POST'])
def control_servo():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({'message': 'Invalid request'}), 400

    angle = data.get('angle')

    if angle is not None:
        try:
            angle = int(angle)
        except (ValueError, TypeError):
            return jsonify({'message': 'Invalid angle'}), 400

        if 0 <= angle <= 180:
            setAngle(angle)
            return jsonify({
                'message': 'angle set to {}'.format(angle)
            })
        else:
            return jsonify({
                'message': 'Angle must be between 0 and 180'
            }), 400
    else:
        return jsonify({
            'message': 'fail! check your parameter'
        }), 400


if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5001)
    finally:
        servo.stop()
        GPIO.cleanup()
