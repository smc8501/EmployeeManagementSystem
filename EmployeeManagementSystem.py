'''
Created on 22 Oct 2022

@author: sofiamc
'''

import sqlite3
from Employee import Employee

conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute("""CREATE TABLE employees (first text, last text, pay real)""")
def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first':emp.first, 'last':emp.last, 'pay': emp.pay})
def get_emps_by_name(lastname):
        c.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
        return c.fetchall()
def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay 
                    WHERE first = :first AND last = :last""", {'first': emp.first, 'last': emp.last, 'pay': pay})
def remove_emp(emp):
    with conn:
        c.execute("DELETE from employees WHERE first = :first AND last = :last", 
                  {'first': emp.first, 'last': emp.last})



emp_1 = Employee("Jeanne", "Godfrey", 12000)
emp_2 = Employee("John", "Doe", 80000)
emp_3 = Employee("Jane", "Doe", 90000)
emp_4 = Employee("Corey", "Schafer", 30000)
emp_5 = Employee("Mary", "Schafer", 40000)

insert_emp(emp_1)
insert_emp(emp_2)
insert_emp(emp_3)
insert_emp(emp_4)
insert_emp(emp_5)

update_pay(emp_2, 20000)
querEmp = get_emps_by_name("Doe")
print(querEmp)





conn.close()