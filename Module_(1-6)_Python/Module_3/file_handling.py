"""
file = open('name.txt', 'r')
content = file.read()
print(content)
file.close()
"""

with open('name.txt', 'r') as file:
    content = file.read()
    print(content)

with open('name.txt', 'a') as wr:
     wr.write("Hello Sohana Arifin \n")
     wr.write("I am you boy \n")