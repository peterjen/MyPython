class D21_Employee:
    rate = 1.05
    def __init__(self,fname,lname,salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

    def email(self):
        return '{}.{}@email.com'.format(self.fname,self.lname)
        #self.email = '{}.{}@email.com'.format(self.fname,self.lname)
    @property
    def fullname(self):
        return '{} {}'.format(self.fname,self.lname)

    def apply_raise(self):
        self.salary = self.salary * self.rate

#emp_1 = D21_Employee('Corey','Schafer',52500)
#print(emp_1.email())
