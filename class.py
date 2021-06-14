class employee:
    pass

emp_1 = employee()
emp_2 = employee()


# print(emp_1)
# print(emp_2)

emp_1.first = 'adil'
emp_1.second = 'a'
emp_1.email = 'mohdadil3977@gmail.com'

# emp_1.pay = 5000


emp_2.first = 'test'
emp_2.second = 't'
emp_2.email = 'test@gmail.com'

emp_2.pay = 10000

print(emp_1.email)
print(emp_2.pay)

# class with 

class Employee:

    def __init__(self, pay, second):
        self.pay=pay
        # self.email= first + '.' + second + '@gmail.com'        
        self.first= 'Adil_af4'
        self.second=second
    def full_name(self):
        return '{} {}'.format(self.first, self.second)
empl_1 = Employee(6000, 'a')
# print(empl_1) 
# print(empl_1.first)

# print(empl_1.full_name())

#full name can also be call by class name

print(Employee.full_name(empl_1))


class templ:

    def __init__(adl, self, add, idnum):
        adl.self = self
        adl.add = add
        adl.idum = idnum

temporary = templ('keshav', 'msk_mill', 555)



print(temporary.self, temporary.add)
print(temporary.idum) 



