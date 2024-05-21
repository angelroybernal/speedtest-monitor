import os
import time
import sqlite3
from datetime import datetime
import schedule
import internet_speed_test

def start_db():
    con = sqlite3.connect("monitor.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE internet_speed(time, upload, download)")

def job():
    con = sqlite3.connect("monitor.db")
    cur = con.cursor()
    print('Probando...')
    internet_speed_now = internet_speed_test.test_internet_speed()
    print('Guardando los resultados...')
    data = (datetime.now() , internet_speed_now['upload'], internet_speed_now['download'])
    cur.execute("INSERT INTO internet_speed VALUES(?, ?, ?)", data)
    con.commit()

if not os.path.isfile("monitor.db"):
    start_db()

schedule.every(15).minutes.do(job)
while True:
    schedule.run_pending()
    time.sleep(60)