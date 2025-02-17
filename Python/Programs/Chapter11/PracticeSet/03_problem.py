class Employee:
       salary = 234
       increment = 20
       
       @property
       def salaryAfterincrement(self):
              return (self.salary+self.salary+(self.increment/100))
       
       @salaryAfterincrement.setter
       def salaryAfterincrement(self,salary):
              self.increment = ((salary/self.salary)-1) *100



e=Employee()
e.salaryAfterincrement=280
print(e.increment)
