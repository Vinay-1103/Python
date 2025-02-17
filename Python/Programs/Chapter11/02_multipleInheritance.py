class Employee:
    company = "ITC"
    name ="Vinay"

    def show(self):
        print(f"The name of the employee is {self.name} and the company is {self.company}")

class Coder:
    language ="Python"
    def printLanguage(self):
        print(f"The language here is {self.language}")

class Programmer(Employee,Coder):
     # company ="ITC infotech"

    def showLanguage(self):
        print(f"the name is {self.company} and he is good with {self.language}")

a=Employee()
b=Programmer()

b.show()
b.printLanguage()
b.showLanguage()