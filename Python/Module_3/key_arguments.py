"""
def my_fun(f_name, l_name, age):
    print(f"My name is {f_name} {l_name}. I am {age} years old")

my_fun(age=25,f_name='abir', l_name='hasan')
"""
#arbitary Number of key word arguments
def my_fun(**kwargs):
    print(kwargs)

    print(f"My name is {kwargs['f_name']} {kwargs['l_name']}. I am {kwargs['age']} years old")

my_fun(age=25,f_name='abir', l_name='hasan')
