import unittest
from D21_employee import D21_Employee
#https://www.youtube.com/watch?v=6tNS--WetLI&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=21
class test_class(unittest.TestCase):

    def test_email(self):
        #print('test_email')
        emp_1 = D21_Employee('Corey','Schafer',50000)
        emp_2 = D21_Employee('Sue','Smith',60000)

        self.assertEqual(emp_1.email(), 'Corey.Schafer@email.com')
        self.assertEqual(emp_2.email(), 'Sue.Smith@email.com')

        emp_1.fname = 'John'
        emp_2.fname = 'Jane'

        self.assertEqual(emp_1.email(), 'John.Schafer@email.com')
        self.assertEqual(emp_2.email(), 'Jane.Smith@email.com')

    def test_fullname(self):
        #print('test_fullname')
        emp_1 = D21_Employee('Corey','Schafer',50000)
        emp_2 = D21_Employee('Sue','Smith',60000)

        self.assertEqual(emp_1.fullname, 'Corey Schafer')
        self.assertEqual(emp_2.fullname, 'Sue Smith')

        emp_1.fname = 'John'
        emp_2.fname = 'Jane'

        self.assertEqual(emp_1.fullname, 'John Schafer')
        self.assertEqual(emp_2.fullname, 'Jane Smith')

    def test_apply_raise(self):
        #print('test_apply_raise')
        emp_1 = D21_Employee('Corey','Schafer',50000)
        emp_2 = D21_Employee('Sue','Smith',60000)

        emp_1.apply_raise()
        emp_2.apply_raise()

        self.assertEqual(emp_1.salary, 52500)
        self.assertEqual(emp_2.salary, 63000)


if __name__ == '__main__':
    unittest.main()