from fibo import Fibonacci

def display_menu():
    print("\nChoose an option:")
    print("1. Generate Fibonacci series by number of terms")
    print("2. Generate Fibonacci series by maximum value")
    print("3. Exit")

def main():
    fib = Fibonacci()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            n = int(input("Enter the number of terms: "))
            fib.number_term(n)
        elif choice == '2':
            max_val = int(input("Enter the maximum value: "))
            fib.maximum_value(max_val)
        elif choice == '3':
            fib.exit()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
