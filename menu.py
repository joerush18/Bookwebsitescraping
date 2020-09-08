from app import details


def best_books():
    print('_____Best Books______')
    books = sorted(details, key=lambda x: x.rating * -1)[:10]
    for book in books:
        print(book)


def cheapest_books():
    print('_____Cheapest  Books______')
    books = sorted(details, key=lambda x: x.price)[:10]
    for book in books:
        print(book)


def next_book():
    print(next(book for book in details))  # iterable


def menu():
    print(Menu_items)
    User_choice = input("Enter Your Choice")
    while User_choice != 'e':
        if User_choice in ('b', 'c', 'n'):
            MENU_CHECK[User_choice]()

        else:
            print("Please Input proper Value")

        print(Menu_items)
        User_choice = input("Enter You Choice")
    else:
        print("Exiting")


Menu_items = '''
Enter 'b' for best books.
Enter 'c' for Cheapest books.
Enter 'n' for Next book.
Enter 'e' to exit
'''

MENU_CHECK = {
    'b': best_books,
    'c': cheapest_books,
    'n': next_book
}

menu()
