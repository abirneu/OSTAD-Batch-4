
try: #je code e error thakte pare
    with open('name.txt', 'r') as f:
        print(f.read())
        print(10/0)
        x= int("sdaf")
        a=[1,2,3]
        print(a[100])
        x =asdf
except FileNotFoundError:
    print("file not found")
except ZeroDivisionError:
    print("Division by Zero is not possible")
except ValueError:
    print("string is not int")
except IndexError:
    print("Index is not present")
except Exception as e:
    print("Some error occured!!",e)

#Custom error handling
try:
    check_file('data.csv')
except Exception as e:
    print(e)














