import json
import sqlite3

def create_tables(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    conn = sqlite3.connect('exemple.db')
    cursor = conn.cursor()

    for table in data:
        sql = '''CREATE TABLE {} (
        '''.format(table)
        for field in data[table]:
            sql += '{},'.format(field)
        sql = sql[:-1] + '''
        );'''
        cursor.execute(sql)
    conn.commit()
    conn.close()
    
create_tables(file_path)
