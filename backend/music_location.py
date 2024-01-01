from datetime import datetime
import sqlite3
import propertiesUtil
import propertiesContents
import globUtil

dbname = propertiesUtil.read_properties(propertiesContents.DB_PATH)
music_folder = propertiesUtil.read_properties(propertiesContents.MUSIC_FOLDER)

        # conn = sqlite3.connect("wiki.db")
        # c = conn.cursor()
        # try:
        #     c.execute("DELETE FROM tango where text = '要対処'")
        #     conn.commit()
        # except sqlite3.IntegrityError as e:
        #     print(e)
        #     print("Error code:", e.sqlite_errorcode)
        #     assert e.sqlite_errorcode == sqlite3.SQLITE_CONSTRAINT_UNIQUE
        #     print("Error name:", e.sqlite_errorname)
        #     conn.rollback()
        # conn.close()
def create_table():
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    try:
        cur.execute(
            'CREATE TABLE music_location(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING, path STRING, created timestamp default current_timestamp, updated timestamp default current_timestamp)')
        conn.commit()
    except:
        pass
    conn.close()

def get_all():
    create_table()
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    cur.execute(
        'SELECT * FROM music_location')
    lists = []
    for row in cur:
        s = []
        # id
        s.append(row[0])
        # name
        s.append(row[1])
        # path
        s.append(row[2])
        lists.append(s)
    conn.close()
    return lists

def insert_search_all():
    print(music_folder)
    music_list = []
    for file in globUtil.search_sub_folder(music_folder, "wav"):
        s = []
        s.append(file)
        replace_file_name = file.replace(music_folder + "\\", "")
        replace_file_name = replace_file_name.replace(".wav", "")
        s.append(replace_file_name)
        music_list.append(s)
        
    for file in globUtil.search_sub_folder(music_folder, "mp3"):
        s = []
        s.append(file)
        replace_file_name = file.replace(music_folder + "\\", "")
        replace_file_name = replace_file_name.replace(".mp3", "")
        s.append(replace_file_name)
        music_list.append(s)

    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    # try:
    # sqliteはtruncateなし　dropで指定なしなら処理を軽くなっている
    conn.execute("DELETE FROM music_location")
    conn.commit()
    conn.execute("DELETE FROM sqlite_sequence WHERE name = 'music_location'")
    conn.commit()
    # except:
    #     pass
    try:
        # 登録できるだけ登録
        conn.executemany( "INSERT INTO music_location( path, name ) VALUES ( ?, ? )",  music_list )
    except:
        pass
    finally:
        conn.commit()
    cur = conn.cursor()
    cur.execute(
        'SELECT * FROM music_location')
    replace_music_list = []
    for row in cur:
        s = []
        # id
        s.append(row[0])
        # name
        s.append(row[1])
        # path
        s.append(row[2])
        replace_music_list.append(s)
    
    conn.close()
    return replace_music_list



def search(searchWord):
    lists = []

    conn = sqlite3.connect(dbname)
    cur = conn.cursor()

    print(searchWord)
    searchMethod = f'SELECT * FROM music_location WHERE name = "{searchWord}"'
    cur.execute(
        searchMethod
    )
    # for row in cur:
    #     antWord = row[3]

    conn.close()

    return lists
