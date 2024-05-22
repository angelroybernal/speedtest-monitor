import os
import time
import sqlite3
from flask import Flask, render_template

import os
app = Flask(__name__)

_port = os.environ.get('PORT', 5000)

@app.route('/')
def dashboard():
    con = sqlite3.connect("../monitor.db")
    cur = con.cursor()
    res = cur.execute("SELECT * FROM internet_speed ORDER BY time DESC LIMIT 24")
    data = res.fetchall()
    con.close()

    chart_data = {
        'labels' : [sub[0] for sub in data],
        'upload' : [sub[1] for sub in data],
        'download' : [sub[2] for sub in data]
    }

    return render_template('index.html', chart_data=chart_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=_port, debug=True)
