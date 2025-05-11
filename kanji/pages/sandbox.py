import streamlit as st
import sqlitecloud
import pandas as pd
import json
import sys
import os

# Get the directory one level above the current running file
parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Add the parent directory to sys.path
sys.path.insert(0, parent_directory)

import kanji
# Open the connection to SQLite Cloud
myfile = '0d7bcc546a68d2b7a16ef6582f6bbf41.csv'
my_table = 'kanji_table'
test = kanji.GuessingGame(f'users/{myfile}')

connection = "sqlitecloud://ceahtcwnhz.g3.sqlite.cloud:8860/chinook.sqlite?apikey=W9ozghn1Za5h0TyHNCN4Vt9Fgmarkkd5JII0F6bgQsg"
conn = sqlitecloud.connect(connection)

cursor = conn.cursor()

# Create a table
cursor.execute(f'''
CREATE TABLE IF NOT EXISTS {my_table} (
    id TEXT PRIMARY KEY,
    data TEXT
)
''')

cursor.execute(f"SELECT id FROM {my_table} WHERE id = ?", myfile)
row = cursor.fetchone()
blah = json.dumps(test.mydict)

if row:
    cursor.execute(f"UPDATE {my_table} SET data = ? WHERE id = ?", (blah, myfile))
else:
    cursor.execute(f"INSERT INTO {my_table} (id, data) VALUES (?,?)", (myfile, blah))

conn.commit()

cursor = conn.execute(f'SELECT * FROM {my_table}')
headers = [desc[0] for desc in cursor.description]
result = cursor.fetchone()[1]

#df = pd.DataFrame(result,columns=headers)

x = json.loads(result[1])
st.write(x)



conn.close()

st.write(test.mydict)