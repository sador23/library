class Person():
    def __init__(self, name, email, age, password):
        self.name = name
        self.password = password
        self.age = age
        self.email = email
        self.status = ""

    def get_status(self):
        return self.status

    def get_attr_list(self):
        attr_list = []
        attr_list.extend([self.name, self.email, self.age, self.password, self.status])
        return attr_list


class Student(Person):
    def __init__(self, name, email, age, password):
        super().__init__(name, email, age, password)
        self.status = "Student"
        self.reserve_list = []

    def reserve(self, list_book):
        self.reserve_list.append(list_book)


class admin(Person):
    def __init__(self, name, email, age, password):
        super().__init__(name, email, age, password)
        self.status = "admin"
