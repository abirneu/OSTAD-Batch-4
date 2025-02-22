class School:
    school_name= "ABC school"
    @staticmethod
    def calculate_grade(marks):
        if marks >=80:
            return 'A'
        else:
            return 'F'
marks= 0
temp = School.calculate_grade(marks)
print(temp)