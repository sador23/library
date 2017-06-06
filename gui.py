import tkinter
from tkinter import messagebox
from tkinter import *
import commands
from tkinter import scrolledtext

class gui():
    def __init__(self, root):
        self.reserve_books = None
        self.admin_search = None
        self.root=root
        # images
        imageback = PhotoImage(file="third.png", width=1400, height=1400)
        imagestudent = PhotoImage(file="first.png", width=1400, height=1400)
        image_admin = PhotoImage(file="admin.png", width=1400, height=1400)
        image_register = PhotoImage(file="register.png", width=1400, height=1400)

        # frames
        self.frame_first = tkinter.Canvas(root, width=700, height=700)
        self.frame_first.pack()
        self.frame = tkinter.Label(self.frame_first, width=700, height=700, image=imageback)
        self.frame.image = imageback
        imageback.subsample(70)
        self.frame.pack()
        self.registerframe = tkinter.Label(self.frame, width=700, height=700, image=image_register)
        self.registerframe.image = image_register
        self.loginframe = tkinter.Label(self.frame, width=700, height=700, image=imageback)
        self.loginframe.image = imageback
        self.loginframe.grid_anchor("center")
        self.loginframe.grid_propagate(False)
        self.registerframe.grid_propagate(False)
        self.adminframe = tkinter.Label(self.frame, width=700, height=700, image=image_admin)
        self.adminframe.image = image_admin
        self.studentframe = tkinter.Label(self.frame, width=700, height=700, image=imagestudent)
        self.studentframe.image = imagestudent
        self.adminframe.grid_propagate(False)
        self.studentframe.grid_propagate(False)
        self.registerframe.grid_anchor("n")
        self.adminframe.grid_anchor("center")

        # registerframe:
        self.reg_button = tkinter.Button(self.registerframe, text="Register", command=commands.Commands.register,
                                         anchor=CENTER)
        # entries
        self.reg_button.grid(row=8, column=1)
        self.name_text = tkinter.Entry(self.registerframe)
        self.name_text.grid(row=1, column=1)
        self.age_text = tkinter.Entry(self.registerframe)
        self.age_text.grid(row=3, column=1)
        self.email_text = tkinter.Entry(self.registerframe)
        self.email_text.grid(row=5, column=1)
        self.psword_text = tkinter.Entry(self.registerframe, show="*")
        self.psword_text.grid(row=7, column=1)
        self.reg_back_button = tkinter.Button(self.registerframe, text="Back", command=commands.Commands.go_back)
        self.reg_back_button.grid(row=8, column=2)

        # labels
        gui.label_factory(self.registerframe, 0, 1, "Enter name here")
        gui.label_factory(self.registerframe, 2, 1, "Enter age here")
        gui.label_factory(self.registerframe, 4, 1, "Enter email here")
        gui.label_factory(self.registerframe, 6, 1, "Enter password here")

        # Login frame:
        gui.label_factory(self.loginframe, 0, 1, "Enter name")
        gui.label_factory(self.loginframe, 2, 1, "Enter password")
        gui.label_factory(self.loginframe, 3, 2, "Not a member yet?")
        self.login_name = tkinter.Entry(self.loginframe)

        self.login_name.grid(row=1, column=1)
        self.login_pass = tkinter.Entry(self.loginframe, show="*")
        self.login_pass.grid(row=3, column=1)

        self.but_log = tkinter.Button(self.loginframe, text="Login", command=commands.Commands.login)
        self.but_log.grid(row=4, column=1)
        self.but_reg = tkinter.Button(self.loginframe, text="Register", command=commands.Commands.new_account)
        self.but_reg.grid(row=4, column=2)
        # self.loginframe.place(x=300,y=250)
        self.loginframe.pack()

        # student frame
        gui.label_factory(self.studentframe, 0, 0, "Search for books")
        self.student_text = tkinter.Entry(self.studentframe)
        gui.label_factory(self.studentframe, 2, 0, "Search by:")
        self.student_options = tkinter.Listbox(self.studentframe)
        self.student_options.insert(1, "Title")
        self.student_options.insert(2, "Author")
        self.student_options.insert(3, "ISBN")
        self.student_options.insert(4, "Year")
        self.student_options.grid(row=3, column=0)
        self.student_text.grid(row=1, column=0)
        self.student_search = tkinter.Button(self.studentframe, text="Search",
                                             command=commands.Commands.search_for_books)
        self.student_search.grid(row=1, column=1)
        gui.label_factory(self.studentframe, 4, 0, "List of books:")
        self.student_book_isbn = tkinter.Entry(self.studentframe)
        self.student_book_isbn.grid(row=2, column=2)
        self.have_books = tkinter.Button(self.studentframe, text="Show reserved books",
                                         command=commands.Commands.show_books).grid(row=2, column=1)
        self.student_scrollbar = tkinter.scrolledtext.ScrolledText(self.studentframe, width=60, height=15)
        self.student_scrollbar.grid(row=4, column=0, columnspan=2, rowspan=2, pady=10)
        self.student_logout_button = tkinter.Button(self.studentframe, text="Log Out",
                                                    command=commands.Commands.log_out)
        self.student_logout_button.grid(row=0, column=2)
        self.student_reserve_button = tkinter.Button(self.studentframe, text="Reserve book",
                                                     command=commands.Commands.reserve)
        self.student_reserve_button.grid(row=3, column=2)

        # adminframe:
        self.admin_button = Button(self.adminframe, text="Search", command=commands.Commands.search_for_users)
        self.admin_button.grid(row=1, column=1)
        gui.label_factory(self.adminframe, 0, 0, "Search for :")
        gui.label_factory(self.adminframe, 2, 0, "Options:")
        self.admin_logout = Button(self.adminframe, text="Log out", command=commands.Commands.log_out).grid(row=0,
                                                                                                            column=2)
        self.admin_entry = Entry(self.adminframe)
        self.admin_entry.grid(row=1, column=0)
        self.admin_options = tkinter.Listbox(self.adminframe)
        self.admin_options.insert(1, "Name")
        self.admin_options.insert(2, "Email")
        self.admin_options.insert(3, "Age")
        self.admin_options.grid(row=3, column=0)
        self.admin_scrollbar = tkinter.scrolledtext.ScrolledText(self.adminframe, width=60, height=15)
        self.admin_scrollbar.grid(row=4, column=1, columnspan=2, rowspan=2)

    def update(self,number):
        if number==1:
            self.but_log.invoke()




    @staticmethod
    def label_factory(frame, row_label, col, text_in):
        new_label = tkinter.Label(frame, text=text_in).grid(row=row_label, column=col)
        return new_label

    def set_to_register(self):
        self.registerframe.pack()
        self.loginframe.pack_forget()
        self.adminframe.pack_forget()
        self.studentframe.pack_forget()

    def set_to_login(self):
        self.registerframe.pack_forget()
        self.loginframe.pack()
        self.adminframe.pack_forget()
        self.studentframe.pack_forget()

    def set_to_student(self):
        self.registerframe.pack_forget()
        self.loginframe.pack_forget()
        self.adminframe.pack_forget()
        self.studentframe.pack()

    def set_to_admin(self):
        self.registerframe.pack_forget()
        self.loginframe.pack_forget()
        self.adminframe.pack()
        self.studentframe.pack_forget()

    def get_login_list(self):
        login = []
        login.extend([self.login_name.get(), self.login_pass.get()])
        self.login_name.delete(0, END)
        self.login_pass.delete(0, END)
        return login

    def error_message(self, msg):
        tkinter.messagebox.showinfo("Error", msg)

    def get_register_list(self):
        name = self.name_text.get()
        self.name_text.delete(0, END)
        age = self.age_text.get()
        self.age_text.delete(0, END)
        password = self.psword_text.get()
        self.psword_text.delete(0, END)
        email = self.email_text.get()
        self.email_text.delete(0, END)
        if (not name) or (not age) or (not password) or (not email):
            return []
        if self.checkvalidity(name, email, age, password):
            return [name, email, age, password]
        else:
            return []

    def checkvalidity(self, name, email, age, password):
        try:
            age_int = int(age)
            pass_int = int(password)
            if age_int < 14 or age_int > 120:
                return False
            if len(password) < 4 or len(password) > 8:
                return False
        except ValueError:
            return False

        if len(name) < 6:
            return False
        return True

    def clear_scrolltext(self):
        self.student_scrollbar.delete(1.0, END)

    def set_scrolltext(self, msg):
        self.student_scrollbar.delete(1.0, END)
        self.student_scrollbar.insert(tkinter.INSERT, msg)

    def get_book_search(self):
        option = self.student_options.curselection()
        option_text = self.student_options.get(option)
        return option_text

    def get_admin_search(self):
        text_admin = self.admin_entry.get()
        self.admin_entry.delete(0, END)
        return text_admin

    def get_admin_option(self):
        option = self.admin_options.curselection()
        option_text = self.admin_options.get(option)
        return option_text

    def set_admin_scroll(self, msg):
        self.admin_scrollbar.delete(1.0, END)
        self.admin_scrollbar.insert(tkinter.INSERT, msg)

    def student_search_text(self):
        text_of_student = self.student_text.get()
        self.student_text.delete(0, END)
        return text_of_student

    def get_student_reserve(self):
        reserve = self.student_book_isbn.get()
        return reserve

    def option_factory(self, number, name):
        if number == 0:
            self.reserve_books = Listbox(self.studentframe)
            self.reserve_books.grid(row=3, column=1)
        self.reserve_books.insert(number, name)

    def message(self, msg):
        tkinter.messagebox.showinfo("Success", msg)

    def get_reserve_option(self):
        if self.reserve_books.curselection():
            option = self.reserve_books.curselection()
            option_text = self.reserve_books.get(option)
            return option_text
        else:
            return ""

    def clear_text(self):
        self.reserve_books.delete(0, END)
        self.student_text.delete(0, END)
        self.student_scrollbar.delete(1.0, END)
        self.admin_scrollbar.delete(1.0, END)
        self.admin_entry.delete(0, END)

    def get_admins_option(self):
        if self.admin_search.curselection():
            option = self.admin_search.curselection()
            option_text = self.admin_search.get(option)
            return option_text
        else:
            return ""

    def search_factory(self, number, name):
        if number == 0:
            self.admin_search = Listbox(self.adminframe)
            self.admin_search.grid(row=1, column=2)
        self.admin_search.insert(number, name)
