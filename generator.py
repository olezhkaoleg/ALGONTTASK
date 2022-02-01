#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      olezhkaoleg
#
# Created:     30.01.2022
# Copyright:   (c) olezhkaoleg 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sqlite3


def load_data():
    with sqlite3.connect("mydatabase.db") as db:
        pass
    cursor = db.cursor()

    sql = "SELECT CPU.CPU_percent, CPU.Current_time FROM CPU ORDER BY CPU.Current_time DESC LIMIT 720"
    cursor.execute(sql)
    data = cursor.fetchall()
    print(data)
    return data

if __name__ == '__main__':
    load_data()
