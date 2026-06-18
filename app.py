from flask import Flask, render_template, jsonify
import sensor
import database
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/data')
def get_data():
    return jsonify(database.get_readings())

if __name__ == '__main__':
    database.create_table()
    app.run(host='0.0.0.0', port=5000, debug=True)
