# Bridge Health Monitoring System

This project uses Arduino Nano 33 BLE Sense and Edge Impulse to detect structural anomalies in bridge vibrations.

## Features
- On-device ML classification: "Normal" vs. "Damage"
- Real-time visualization via Flask API and web dashboard
- USB serial communication for data transmission

## Tech Stack
- Arduino + C++
- Edge Impulse
- Python Flask
- HTML + JavaScript

## How to Run
1. Train and export ML model via Edge Impulse
2. Upload firmware to Nano 33 BLE
3. Start Flask server: `python server.py`
4. Visit `http://127.0.0.1:5000` to view real-time dashboard

## Team
- Iwanthi Abeysinghe 
- Janani Amarathunga 
- Chamodya Morapitiya
- Ridma Jayawardena
  
