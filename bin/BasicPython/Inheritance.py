class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def get_name(self):
        return f"{self.firstname}, {self.lastname}"

class Student(Person):
    def __init__(self, school, fname, lname):
        super().__init__(fname, lname)
        self.school = school

    def get_school(self):
        return self.school

x = Person("John", "Doe")
print(x.get_name())

y = Student("Yettacode", "Vinodh", "Francis")
print(y.get_name())
print(y.get_school())
