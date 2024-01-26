# This is a library management system
# using sqlite3 to create to tables that stores books abd borrowed books in a library
# This system is effective in inventory management of the books


import sqlite3 as sq
import random as rd

# connecting to a database
db = sq.connect('books_db')
print('Connection established!')

# creating a cursor object to allow for SQL commands to execute
cursor = db.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY,
                                        title TEXT NOT NULL UNIQUE,
                                        author TEXT,
                                        genre TEXT,
                                        copies INTEGER NOT NULL)
    
    ''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS books_borrowed(id_books INTEGER PRIMARY KEY,
                                        title TEXT NOT NULL UNIQUE,
                                        user_name TEXT NOT NULL,
                                        user_id INTEGER UNIQUE,
                                        borrowed_date DATE,
                                        return_date DATE
                                        borrowed_copies INTEGER NOT NULL)
''')

db.commit()
print('Tables created!')

# This function adds a new book the library database in the books table
def add_book():
    # book_id = int(input('please enter the book ID: '))
    book_id = rd.randint(1, 10000)

    book_title = input('please enter the book title: ')
    book_author = input('please the book author: ')
    book_genre = input('please enter the book genre: ')
    book_copies = int(input('please enter the amount of copies of the book: '))

    cursor.execute('''
        INSERT INTO books(id, title, author, genre, copies)
                    VALUES(?,?,?,?,?);
    ''', (book_id, book_title, book_author, book_genre, book_copies))

    db.commit()
    print('Book has been added!')

# This function is used for inventory management in the books table
def view_stock():

    cursor.execute('''
        SELECT * FROM books
    ''')

    data = cursor.fetchall()
    print(data)

# This function is updates the book table
def edit_book():
    book_id = input('please enter the book id: ')
    new_title = input('please enter the new book title: ')
    new_author = input('please the new book author: ')
    new_genre = input('please enter the new book genre: ')
    new_copies = int(input('please enter the new amount of copies of the book: '))

    update_books = f'''
    UPDATE books SET title = ?, author = ?, genre = ?,
    copies = ? WHERE id = ?
    '''
    cursor.execute(update_books, (new_title, new_author, new_genre, new_copies, book_id))

    db.commit()
    print('Book has been replaced!')

# This function is used to add borrowed books in the table
def add_borrowed_books():
    book_id = int(input('please enter the book ID: '))
    book_title = input('please enter the book title: ')
    user_name = input('please enter name of the one borrowing the book: ')
    user_id = input('please enter the id of the one borrowing the book: ')
    borrowed_date = input('please enter the date of when the book was borrowed: ')
    return_date = (input('please enter the date of when the book will be returned: '))
    #borrowed_copies = input('please enter the number of the copies borrowed')

    borrowed_books = f'''
    INSERT INTO books_borrowed(id, title, user_name, user_id, borrowed_date,
                             return_date)
     VALUES (?,?,?,?,?,?)                        
    '''

    cursor.execute(borrowed_books, (book_id, book_title, user_name, user_id, borrowed_date,
                                    return_date))

    db.commit()
    print('Book borrowed has been added!')

# This function shows inventory of the borrowed books
def check_borrowed_books():
    cursor.execute('''
    SELECT * FROM books_borrowed
    ''')
    data = cursor.fetchall()
    print(data)

# below is the menu for the user to choose from
while True:
    menu = input('''
    welcome to the library Database! please choose from the menu selection below:
        1 - Add a new book to the database
        2 - Edit a book in the database 
        3 - Manage inventory
        4 - add borrowed books
        5 - check borrowed books
        6 - To exit
    ''')

    if menu == '1':
        add_book()
    elif menu == '2':
        edit_book()
    elif menu == '3':
        view_stock()
    elif menu == '4':
        add_borrowed_books()
    elif menu == '5':
        check_borrowed_books()
    elif menu == '6':
        print('exiting!')
        break
    else:
        print('you did not choose from the list given, try again!')
        continue

print('Thank you for using our library, I hope you had fun!')

