import sqlite3

db_name = "cnf_db"


def make_database():
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS connect (id INTEGER PRIMARY KEY AUTOINCREMENT, from_id int NOT NULL,\
                    target int NOT NULL);")

    cursor.execute("CREATE TABLE IF NOT EXISTS messages (id INTEGER PRIMARY KEY AUTOINCREMENT, from_id int NOT NULL,\
                    target int NOT NULL, message text NOT NULL );")

    conn.close()


def make_connection(chat_id, target_id):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute("select * from connect where from_id='%s';" % (chat_id))
    from_id = cursor.fetchall()

    if len(from_id) == 0:
        cursor.execute(" insert into connect (from_id, target) values ('%d','%d') " % (chat_id, target_id))
        conn.commit()
    else:
        cursor.execute("update connect SET target='%d' WHERE from_id='%d';" % (target_id, chat_id))
        conn.commit()

    conn.close


def get_target(chat_id):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute("select target from connect where from_id='%d';" % (chat_id))
    target = cursor.fetchall()
    return target[0][0]


def save_messages(chat_id, target_id, message):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute(
        " insert into messages (from_id, target, message) values ('%d','%d','%s') " % (chat_id, target_id, message))
    conn.commit()
    conn.close()


def reply_command(chat_id, message):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute("select from_id from messages where target='%d' and message = '%s';" % (chat_id, message))
    target = cursor.fetchall()[-1][0]

    conn.close()

    make_connection(chat_id, target)
