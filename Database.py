import sqlite3
import Person
import hashlib


class data():
    @classmethod
    def __init__(cls, file_name):
        cls.conn = sqlite3.connect('library.db')
        cls.c = cls.conn.cursor()
        # cls.c.execute("DROP TABLE IF EXISTS books")
        cls.c.execute(
            '''CREATE TABLE IF NOT EXISTS books (title TEXT,author TEXT, isbn TEXT, type TEXT, page INTEGER, year INTEGER, in_stock TEXT)''')
        cls.c.execute(
            '''CREATE TABLE IF NOT EXISTS users (name TEXT,email TEXT, age INTEGER, password TEXT, status TEXT)''')
        cls.c.execute('''CREATE TABLE IF NOT EXISTS reserve (name TEXT,email TEXT,book TEXT, ISBN TEXT)''')
        # cls.lines=cls.reader(file_name)
        cls.user_list = cls.users()
        cls.curr_user = None

    @classmethod
    def reader(cls, file_name):
        with open(file_name, "r") as reader:
            all_line = reader.readlines()
            length = len(all_line)
            lines = [["" for x in range(0, 7)] for y in range(0, length)]
            for i in range(length):
                line = all_line[i]
                line = cls.line_replacer(line)
                line = line.split(",")
                lines[i][0] = line[1]
                lines[i][1] = line[2]
                lines[i][2] = line[6]
                lines[i][3] = line[10]
                lines[i][4] = line[12]
                lines[i][5] = line[11]
                lines[i][6] = "Available"
                cls.c.execute("INSERT INTO books VALUES (?,?,?,?,?,?,?)", lines[i])
            cls.conn.commit()
            return lines

    @classmethod
    def users(cls):
        user_list = []
        cls.c.execute("SELECT * FROM users")
        fetcher = cls.c.fetchall()
        for i in fetcher:
            if i[4] == "admin" or i[0] == "Gipsz Jakab":
                user_list.append(Person.admin(i[0], i[1], i[2], i[3]))
            else:
                user_list.append(Person.Student(i[0], i[1], i[2], i[3]))
        return user_list

    @classmethod
    def get_person(cls, name):
        cls.c.execute("SELECT * FROM users WHERE name=?", (name,))
        fetcher = cls.c.fetchall()
        if not fetcher:
            return [0, 0, 0, 0, 0]
        fetcher_norm = fetcher[0]
        return fetcher_norm

    @classmethod
    def add_person(cls, list_account):
        cls.c.execute("INSERT INTO users VALUES (?,?,?,?,?)", list_account)
        cls.conn.commit()

    @classmethod
    def append_users(cls, student):
        cls.user_list.append(student)

    @classmethod
    def search(cls, option, option_text, database):
        fresh = option_text
        option_text = "%" + option_text + "%"
        option = option.lower()
        cls.c.execute("SELECT * FROM " + database + " WHERE " + option + " LIKE ?", (option_text,))
        fetch = cls.c.fetchall()
        if not fetch:
            cls.c.execute("SELECT * FROM " + database + " WHERE " + option + " =?", (fresh,))
            fetch = cls.c.fetchall()
        return fetch

    @classmethod
    def line_replacer(cls, line):
        line = line.replace(", #1", "#1")
        line = line.replace(", #2", "#2")
        line = line.replace(", #3", "#3")
        line = line.replace('"=""', '')
        line = line.replace('"""', '')
        line = line.replace(', ', ' ')
        line = line.replace('"', '')
        return line

    @classmethod
    def get_user(cls, name):
        for i in cls.user_list:
            attrs = i.get_attr_list()
            if attrs[0] == name:
                cls.curr_user = i
                return attrs

    @classmethod
    def export_reserve(cls, book1, book2, name, email):
        cls.c.execute("INSERT INTO reserve VALUES(?,?,?,?)", (name, email, book1, book2))
        cls.c.execute("UPDATE books SET in_stock='Not in stock' WHERE isbn=?", (book2,))
        cls.conn.commit()
