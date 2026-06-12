import sqlite3
from datetime import datetime

def create_table():
    conn = sqlite3.connect('readings.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS readings (id INTEGER PRIMARY KEY AUTOINCREMENT, timestamp TEXT, temperature REAL, humidity REAL)")
    conn.commit()
    conn.close()

def insert_reading(temperature, humidity):
    conn = sqlite3.connect('readings.db')
    cursor = conn.cursor()
    timestamp = datetime.now()
    cursor.execute("INSERT INTO readings (timestamp, temperature, humidity) VALUES (?, ?, ?)", (timestamp, temperature, humidity))
    conn.commit()
    conn.close()

def get_readings():
    conn = sqlite3.connect('readings.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM readings")
    readings = cursor.fetchall()
    conn.close()
    return readings
