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
    cursor.execute("SELECT * FROM readings ORDER BY timestamp DESC LIMIT 144")
    readings = cursor.fetchall()
    conn.close()
    return readings[::-1]

def get_stats():
    conn = sqlite3.connect('readings.db')
    cursor = conn.cursor()
    cursor.execute("SELECT MAX(temperature) FROM readings WHERE timestamp >= datetime('now', '-7 days')")
    week_high_temp = cursor.fetchone()[0]
    cursor.execute("SELECT MIN(temperature) FROM readings WHERE timestamp >= datetime('now', '-7 days')")
    week_low_temp = cursor.fetchone()[0]
    cursor.execute("SELECT MAX(temperature) FROM readings WHERE timestamp >= datetime('now', '-30 days')")
    month_high_temp = cursor.fetchone()[0]
    cursor.execute("SELECT MIN(temperature) FROM readings WHERE timestamp >= datetime('now', '-30 days')")
    month_low_temp = cursor.fetchone()[0]
    cursor.execute("SELECT MAX(humidity) FROM readings WHERE timestamp >= datetime('now', '-7 days')")
    week_high_hum = cursor.fetchone()[0]
    cursor.execute("SELECT MIN(humidity) FROM readings WHERE timestamp >= datetime('now', '-7 days')")
    week_low_hum = cursor.fetchone()[0]
    cursor.execute("SELECT MAX(humidity) FROM readings WHERE timestamp >= datetime('now', '-30 days')")
    month_high_hum = cursor.fetchone()[0]
    cursor.execute("SELECT MIN(humidity) FROM readings WHERE timestamp >= datetime('now', '-30 days')")
    month_low_hum = cursor.fetchone()[0]
    conn.close()
    return {
    'week_high_temp': week_high_temp,
    'week_low_temp': week_low_temp,
    'month_high_temp': month_high_temp,
    'month_low_temp': month_low_temp,
    'week_high_hum': week_high_hum,
    'week_low_hum': week_low_hum,
    'month_high_hum': month_high_hum,
    'month_low_hum': month_low_hum
}
