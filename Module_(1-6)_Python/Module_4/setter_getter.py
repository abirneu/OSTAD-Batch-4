class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary= salary # "_" dile seta protected variable hoye jay
        #but logically private hoy na

    def get_salary(self, password):
        if password == "admin":
            print(self._salary)

        else:
            print("Invalid Password")




    

obj1= Employee("Abir",30000)
obj2= Employee("Sohana",40000)

print(obj2)
            


