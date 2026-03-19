class student:
    dept="CSE"
    def set_dim(self,name,marks):
       self.name=name
       self.marks=marks
       self.p=0
    def per(self):
        self.p= sum (self.marks)//3
    def display(self):
        print("1.NAME:",self.name)
        print("2.SCORE:",self.p)
        print("3.DEPT:",student.dept)
        
see=student()
haa=student()
huu=student()
see.set_dim("S",[40,50,60])
haa.set_dim("HA",[46,37,89])
huu.set_dim("HU",[53,56,79])

see.display()
haa.display()
huu.display()