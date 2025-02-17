class Employee:
    company = "ITC"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

class Programmer:
    company = "ITC infotech"
    name = "Vinay"
    language="python"
    def show(self):
        print(f"The name is {self.name} and the language is {self.language}")
     

    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language}")


a=Employee()
b=Programmer()
b.show()

print(a.company,b.company)