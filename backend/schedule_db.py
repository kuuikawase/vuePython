from datetime import datetime
import sqlite3
import propertiesUtil
import propertiesContents
import globUtil

dbname = propertiesUtil.read_properties(propertiesContents.DB_PATH)
SCHEDULE_NOW_TASK_PATH = propertiesUtil.read_properties(propertiesContents.SCHEDULE_NOW_TASK_PATH)

def create_table():
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    try:
        cur.execute(
            'CREATE TABLE schedule_task(id INTEGER PRIMARY KEY AUTOINCREMENT, summary STRING,'\
            'description STRING, alldate_flg Boolean, start_date STRING, end_date STRING,'\
            'del_flg BOOLEAN, created timestamp default current_timestamp, updated timestamp default current_timestamp)')
        conn.commit()
    except:
        pass
    conn.close()

def get_all():
    create_table()
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    cur.execute(
        'SELECT id, alldate_flg, start_date, end_date, summary, description FROM schedule_task WHERE del_flg = False ORDER BY id')
    lists = []
    for row in cur:
        s = []
        # id
        s.append(row[0])
        # alldate_flg 終日かのフラグ
        s.append(row[1])
        # start_date 開始日
        s.append(row[2])
        # end_date 終了日
        s.append(row[3])
        # summary タイトル
        s.append(row[4])
        # description 概要
        s.append(row[5])
        lists.append(s)
    
    conn.close()
    return lists

def insert_search_all():
    schedule_list = []
    s_list = []
    with open(SCHEDULE_NOW_TASK_PATH, mode='r', encoding="utf-8") as f:
        s = f.read().split("\\n")
    for s in s_list:
        i1_lists = s.split("|||")
        i2_lists = []
        if i1_lists[0] == "AllDate":
            i2_lists.append(True)
        else:
            i2_lists.append(False)
        # 開始日
        i2_lists.append(i1_lists[1])
        # 終了日
        i2_lists.append(i1_lists[2])
        # タイトル
        i2_lists.append(i1_lists[3])
        # 概要
        if i1_lists[4] == "Nodata":
            i2_lists.append("")
        else:
            i2_lists.append(i1_lists[4])
        schedule_list.append(i2_lists)
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    # try:
    # sqliteはtruncateなし　dropで指定なしなら処理を軽くなっている
    conn.execute("DELETE FROM schedule_task")
    conn.commit()
    conn.execute("DELETE FROM sqlite_sequence WHERE name = 'schedule_task'")
    conn.commit()
    # except:
    #     pass
    try:
        # 登録できるだけ登録
        conn.executemany( "INSERT INTO schedule_task( alldate_flg, start_date, end_date, summary, description ) VALUES ( ?, ?, ?, ?, ? )",  schedule_list )
    except:
        pass
    finally:
        conn.commit()
    conn.close()
    
    return get_all()

