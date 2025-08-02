#Multilevel inheritance
class GrandFather:
    def __init__(self, color, first_name):
        self.color= color
        self.first_name= first_name
    def gf_method(self):
        print("From GrandFather")

class Father(GrandFather):
    def __init__(self,hobby, color, first_name):
        super().__init__(color, first_name)
        self.hobby= hobby
    def father_method(self):
        print("From Father")

class Children(Father, GrandFather):
    def __init__(self, fashion,hobby, color, first_name):
        super().__init__(hobby, color, first_name)
        self.fashion= fashion



#gf1 = GrandFather("red", "hasan")
#f1 = Father("cricket", "blue", "rahim")  # Pass all required arguments
#print(f"{f1.color}\n{f1.first_name}\n{f1.hobby}")  # Output: blue

c1=Children("Test","cricket", "blue", "rahim")
c1.gf_method()
c1.father_method()
print(c1.fashion, c1.color,c1.hobby,c1.first_name)