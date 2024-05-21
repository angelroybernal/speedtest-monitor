import time
import sqlite3
import pandas as pd
import streamlit as st

while True:
    con = sqlite3.connect("monitor.db")
    df = pd.read_sql_query("SELECT * FROM internet_speed", con)
    con.close()

    st.line_chart(data=df, x='time')
    st.write(df)

    time.sleep(60)