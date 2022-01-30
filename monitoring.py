#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      olezhkaoleg
#
# Created:     29.01.2022
# Copyright:   (c) olezhkaoleg 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import time
import sqlite3
import psutil

with sqlite3.connect('C:\\Users\olezhlaoleg\Documents\python\mydatabase.db') as dbconn:
    pass
cursor = dbconn.cursor()
try:
    cursor.execute("""CREATE TABLE CPU
                  (CPU_percent text, Current_time text)
                    """)
except sqlite3.Error:
    print('Using db')
finally:
    print('çonnect')
dbconn.commit()


class CPU_check():
    def __init__(self, cpu5, time_now):
        self.CPUperfivesec = cpu5
        self.current_time = time_now

    def write_in_db(self):
        appendlist = (str(self.CPUperfivesec), str(self.current_time))
        cursor.execute("INSERT INTO CPU VALUES (?,?)", appendlist)
        dbconn.commit()


timer = 3600
while timer > 0:
    CPUperfivesec = psutil.cpu_percent(interval=5)
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    new_stats = CPU_check(CPUperfivesec, current_time)
    new_stats.write_in_db()
    timer -= 5