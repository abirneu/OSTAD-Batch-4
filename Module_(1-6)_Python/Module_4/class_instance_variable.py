"""
class School:
    school_name="ABC"

    def __init__(self,name):
        self.student_name = name

scl1= School("Abir")
print(scl1.school_name)
print(scl1.student_name)
"""

class Temp:
    temp_value= "This is pre define value"

    def __init__(self,value):
        self.temp_value_pass= value
temp1= Temp("This is passing value")
print(temp1.temp_value)
print(temp1.temp_value_pass)
