import sqlite3
import datetime
import socket
import os
import sys


class SqliteDatabase:

    def __init__(self):
        if os.path.exists("gameplay.db"):
            os.remove("gameplay.db")
        self.con = sqlite3.connect('gameplay.db')
        self.cur = self.con.cursor()
        self.cur.execute(
            '''CREATE TABLE game_main (gid integer primary key autoincrement, time text, ip text, wordle text)''')
        self.cur.execute(
            '''CREATE TABLE game_details (gid integer primary key autoincrement, time text, attempt integer, input text, wordle text, log text, foreignid integer, foreign key(foreignid) references game_main(gid))''')
        self.cur.execute('''CREATE TABLE game_statistics (gid integer primary key autoincrement, time text, win_status text, number_of_games integer, win_percentage integer, guesses text, foreignid integer, foreign key(foreignid) references game_main(gid))''')
        self.prev_id = 0

    def extract_ip(self):
        st = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            st.connect(('10.255.255.255', 1))
            IP = st.getsockname()[0]
        except Exception:
            IP = '127.0.0.1'
        finally:
            st.close()
        return IP

    def insert_in_game_main(self, wordle):
        current_time = datetime.datetime.now()
        sock = self.extract_ip()
        self.cur.execute(
            "insert into game_main values (null, ?, ?, ?)", (current_time, sock, wordle))
        self.prev_id = self.cur.lastrowid

    def insert_in_game_details(self, attempt, input_word, wordle, log):
        current_time = datetime.datetime.now()
        self.cur.execute(
            "insert into game_details values (null, ?, ?, ?, ?, ?, ?)", (current_time, attempt, input_word, wordle, log, self.prev_id))

    def insert_in_game_statistics(self, win_status, number_of_games, win_percentage, guesses):
        current_time = datetime.datetime.now()
        self.cur.execute(
            "insert into game_statistics values (null, ?, ?, ?, ?, ?, ?)", (current_time, win_status, number_of_games, win_percentage, guesses, self.prev_id))

    def end(self):
        self.con.commit()
        print("Records created successfully")
        self.con.close()

    def analyze(self, startdate, enddate):
        if not os.path.exists("report.txt"):
            file = open('report.txt', 'a+')
        self.cur.execute(
            "SELECT * FROM 'game_main' where time between :startdate and :enddate", {"startdate": startdate, "enddate": enddate})
        temp = self.cur.fetchall()
        with open('report.txt', 'w') as f:
            f.write(str(temp))
        print(
            f"\nReport generated successfully for date range entered between {startdate} and {enddate} \n")
