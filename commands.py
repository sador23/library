from Database import data
from Person import Student, admin
import hashlib
import uuid

class Commands():
    @classmethod
    def __init__(cls, gui):
        cls.gui = gui
        cls.name = ""

    @classmethod
    def register(cls):
        account_list = cls.gui.get_register_list()
        student = None
        if not account_list:
            cls.gui.error_message("Not a valid input, try again!")
        else:
            account_list[3] = cls.hash_pass(account_list[3])
            if account_list[0] != "Gipsz Jakab":
                student = Student(account_list[0], account_list[1], account_list[2], account_list[3])
            else:
                student = admin(account_list[0], account_list[1], account_list[2], account_list[3])
            data.append_users(student)
            list_of_attr = student.get_attr_list()
            data.add_person(list_of_attr)
            cls.gui.set_to_login()

    @classmethod
    def login(cls):
        cls.gui.set_to_student()
        '''
        login_list = cls.gui.get_login_list()
        person = data.get_person(login_list[0])
        cls.name = person[0]

        if cls.check_password(person[3], login_list[1]):
            if person[4] == "Student":
                cls.gui.set_to_student()
            if person[4] == "admin":
                cls.gui.set_to_admin()
        else:
            cls.gui.error_message("Wrong username or password!")'''

    @classmethod
    def new_account(cls):
        cls.gui.set_to_register()

    @classmethod
    def search_for_books(cls):
        option = cls.gui.get_book_search()
        option_text = cls.gui.student_search_text()
        search_list = data.search(option, option_text, "books")
        plain_text = ""
        header = ["Title: ", "Author: ", "ISBN: ", "Type: ", "Date: ", "Pages: "]
        length = len(search_list)
        for i in range(len(search_list)):
            for j in range(0, 6):
                plain_text += header[j] + str(search_list[i][j]) + "\n"
            plain_text += "\n--------------\n"
            cls.gui.option_factory(i, search_list[i][0])
        cls.gui.set_scrolltext(plain_text)

    @classmethod
    def search_for_users(cls):
        header = ["Name: ", "Email: ", "Age: ", "Reserved: "]
        option = cls.gui.get_admin_option()
        option_text = cls.gui.get_admin_search()
        search_list = data.search(option, option_text, "users")
        plain_text = ""
        length = len(search_list)
        for i in range(length):
            reserve = data.search("name", search_list[i][0], "reserve")
            for j in range(0, 3):
                plain_text += header[j] + str(search_list[i][j]) + "\n"
            if len(reserve) > 1:
                for h in range(len(reserve)):
                    plain_text += header[3] + str(reserve[h][2]) + "\n"
            cls.gui.search_factory(i, search_list[i][0])
            plain_text += "\n--------------\n"
        cls.gui.set_admin_scroll(plain_text)

    @classmethod
    def log_out(cls):
        cls.gui.clear_scrolltext()
        cls.gui.set_to_login()

    @classmethod
    def reserve(cls):
        isbn = cls.gui.get_reserve_option()
        book = data.search("title", isbn, "books")
        user = data.get_user(cls.name)
        if len(book) == 1 and book[0][6] == "Available":
            data.export_reserve(book[0][0], book[0][2], user[0], user[2])
            msg = "Successfully reserved" + book[0][0] + "!"
            cls.gui.message(msg)
            cls.gui.clear_text()
        elif book[0][6] != "Available":
            cls.gui.error_message("Sorry, that book is not available!")
        else:
            cls.gui.error_message("More than one books selected! Select only one!")

    @classmethod
    def hash_pass(cls, password):
        salt = uuid.uuid4().hex
        return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt

    @classmethod
    def check_password(cls, hashed_password, user_password):
        password, salt = hashed_password.split(':')
        return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()

    @classmethod
    def go_back(cls):
        cls.gui.set_to_login()

    @classmethod
    def show_books(cls):
        user = data.get_user(cls.name)
        reserve = data.search("name", user[0], "reserve")
        plain_text = ""
        header = ["Reserved: "]
        length = len(reserve)
        for i in range(len(reserve)):
            plain_text += header[0] + str(reserve[i][2]) + "\n"
        plain_text += "\n--------------\n"
        cls.gui.set_scrolltext(plain_text)
