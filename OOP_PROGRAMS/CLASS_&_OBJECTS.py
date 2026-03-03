class Student:
    def _init_(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

name = input("Enter name: ")
marks = int(input("Enter marks: "))

s1 = Student(name, marks)
s1.display()