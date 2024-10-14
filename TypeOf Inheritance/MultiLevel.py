class student:

    def getstudent(self):
        self.name = input("name: ")
        self.age = int(input("age : "))
        self.gender = input("gender: ")

class subjects(student):

    def getMarks(self):
        self.studentclass = input("class:  ")
        print(f'Entre the marks of subjects ')
        self.maths = int(input("maths : "))
        self.english = int(input("english: "))
        self.marathi = int(input("marathi: "))

class marks(subjects):

    def display(self):
        print(f'name ={self.name}')
        print(f'age ={self.age}')
        print(f'gender ={self.gender}')
        print(f'classname ={self.studentclass}')
        total_marks = self.maths + self.english + self.marathi
        print(f'Total Marks = {total_marks}')
        
markobj = marks()
markobj.getstudent()
markobj.getMarks()
markobj.display()