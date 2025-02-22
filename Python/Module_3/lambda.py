# anonymous function- unnamed function
from numpy import square, add


def suqare(x):
    return  x*x
print(square(5))

#lambda arguments: expression
square= lambda x: ((x*x)+x-x+x)
print(square(4))

add = lambda a,b,c: a+b+c
print(add(2,3,4))

#sorted using lambda
students = [('abir',5), ('emran',2),('anik',6), ('sayed',4)]
sorted_students= sorted(students,key=lambda x: x[1])
print(sorted_students)

#map(), filter(), reduce()

#Map()
nums= [1,2,3,4]
sq_nums= list(map(lambda x: x*x,nums))
print(sq_nums)

for i in nums:
    print(i*i)

















