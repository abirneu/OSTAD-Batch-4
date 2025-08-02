# Name same but kaj different
#Method Overriding- parent er kono method children e ese
#   onno kichu likha hole seta overloading
class GrandFather:
    def __init__(self):
        self.name= "Hello"
        self.__salary = 30000

    def greet(self):

        print("GrandFather sayes")

class Father(GrandFather):
    def greet(self):
        print(f"{self.name} \n{self._GrandFather__salary}")

class Children(Father):
    def greet(self):
        print("Children sayes")

gf= GrandFather()
f= Father()
c= Children()

gf.greet()
f.greet()
c.greet()


#Method OverLoading

class Cal:
    def mul(self, a,b=20):
        return a+b 

test= Cal()
print(test.mul(10))
print(test.mul(10,50))

