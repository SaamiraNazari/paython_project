cs=[{
    'title':'HTML',
    'teacher':'Nazari'
},
    {
        'title':'Python',
        'teacher':'Hedari'
    },
    {
        'title':'CSS',
        'teacher':'Afshar'
    },
    {
        'title':'Javascript',
        'teacher':'Omrai'
    }
    
]
class User:
    def __init__(self,name,lastname):
        self.name=name
        self.lastname=lastname
    def full(self):
        print(self.name,self.lastname)
        
class Student(User):
    def __init__(self, name, lastname,email):
        super().__init__(name, lastname)
        self.email=email
        self.courses=[]
        
    def fullstudent(self):
        print('I am student')
        super().full()
        
    def printcourses(self):
        if self.courses:
            for cours in self.courses:
             print(cours['title'])
        else:
            print('This user dont have cours')
class Teacher(User):
    def __init__(self, name, lastname,code):
        super().__init__(name, lastname)
        self.code=code
        
    def fullteacher(self):
        print('I am teacher')
        super().full()
        
s1=Student('Samir','Nazari','SAMIRA@GMAIL.COM')
s1.courses.append(cs[0])
s1.fullstudent() 
s1.printcourses()
            