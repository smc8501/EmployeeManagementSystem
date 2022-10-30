'''
Created on 22 Oct 2022

@author: sofiamc
'''
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
    
    def email(self):
        return "{}.{}@email.com".format(self.first, self.last)
    def fullname(self):
        return "{} {}".format(self.first, self.last)
    
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)
    


