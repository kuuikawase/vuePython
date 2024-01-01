from datetime import DateTime
import sqlite3
import propertiesUtil
import propertiesContents

dbname = read_properties(DB_PATH)

def create_table():
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    try:
        cur.execute(
            'CREATE TABLE music_play_list(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING, path STRING)')
        conn.commit()
    except:
        pass
    conn.close()

def search(searchWord):
    antWord = "null"

    conn = sqlite3.connect(dbname)
    cur = conn.cursor()

    print(searchWord)
    searchMethod = f'SELECT * FROM music_location WHERE name = "{searchWord}"'
    cur.execute(
        searchMethod
    )
    for row in cur:
        antWord = row[3]

    conn.close()

    return antWord

