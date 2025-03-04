from book_store import BookStore

def display_menu():
    print("Welcome to Book Store Management System")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Remove Book")
    print("5. Exit")

def main():
    store = BookStore()
    store.load_books()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            store.add_book()
        elif choice == '2':
            store.view_books()
        elif choice == '3':
            store.search_book()
        elif choice == '4':
            store.remove_book()
        elif choice == '5':
            store.save_books()
            print("Exiting... All data saved.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()




