class Employee:
    company_name= "Ostad company"
    def __init__(self, name, salary,age):
        self.name= name
        self.salary= salary
        self.age=age

    def display_info(self):
        print(f"EMP name: {self.name}\nSalary : {self.salary} \nAge: {self.age}")
    @classmethod
    def change_company_name(cls,name):
        cls.company_name= name


ob1= Employee("Abir", 40000,25)
ob1.display_info()
ob1.change_company_name("Company name changed")
print(ob1.company_name)


