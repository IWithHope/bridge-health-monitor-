from flask import Flask, jsonify, render_template
import serial
import threading
from datetime import datetime
import time

SERIAL_PORT = 'COM22' 
BAUD_RATE = 115200

# Start with an error message until Serial connects
latest_prediction = "Waiting for data..."

prediction_log=[]

app = Flask(__name__)

def read_serial():
    global prediction_log
    buffer = ""
    while True:
        try:
            with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1) as ser:
                print(f"[INFO] Connected to {SERIAL_PORT}")
                while True:
                    line = ser.readline().decode('utf-8', errors='ignore').strip()
                    if line == "EI_RESULT_START":
                        now = datetime.now()
                        timestamp = (now.strftime('%Y-%m-%d'), now.strftime('%H:%M:%S'))
                    elif line.startswith("Prediction:"):
                        label = line.replace("Prediction: ", "").strip()
                        prediction_log.append((timestamp[0], timestamp[1], label))
                        if len(prediction_log) > 50:
                            prediction_log.pop(0)
                    elif line == "EI_RESULT_END":
                        buffer = ""
        except Exception as e:
            print(f"[ERROR] Serial error: {e}")
            time.sleep(2)


@app.route("/")
def index():
	return render_template("index.html")

@app.route("/prediction")
def prediction():
	return jsonify(log=prediction_log)

if __name__ == "__main__":
	time.sleep(1)
	threading.Thread(target=read_serial, daemon=True).start()
	app.run(debug=False)