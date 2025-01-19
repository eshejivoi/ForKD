import sqlite3 as sq
from config import DATABASE


class DB_Manager:
    def __init__(self, database):
        self.database = database

    def __executemany(self, sql, data):
        conn = sq.connect(self.database)
        with conn:
            conn.executemany(sql, data)
            conn.commit()

    def __select_data(self, sql, data=tuple()):
        conn = sq.connect(self.database)
        with conn:
            cur = conn.cursor()
            cur.execute(sql, data)
            return cur.fetchall()


if __name__ == '__main__':
    manager = DB_Manager(DATABASE)
