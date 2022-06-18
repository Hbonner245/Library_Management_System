import time
import datetime as dt
current = dt.datetime.now()
current_td = dt.timedelta(
    hours=current.hour,
    minutes=current.minute)

username = input("please enter your name ")
print(current_td)
print("Welcome: " + username)
print("This program  allows you to display, add, search for items. ")

while True:
    time.sleep(2)
    print("-------------")
    user_choice = input("""\n Please select from the following options:
  1. - Display items
  2. - Add New items
  3. - Search for  specifc items
  4. - Exit\n
  """)

    print("")

    if user_choice == "1" or user_choice == "one":
        user_option = input("""\n Please choose what you would like to display:
1. - Display all books
2. - Display all DVD's\n""")
        if user_option == "1" or user_option == "one":
            books_file = open("books.txt", "r")
            book = books_file.read()
            print(f"{book}")
            books_file.close()
        if user_option == "2" or user_option == "two":
            dvd_file = open("dvd.txt", "r")
            dvds = dvd_file.read()
            print(f"{dvds}")
            dvd_file.close()

    if user_choice == "2" or user_choice == "two":
        user_option = input("""\n Please choose what you would like to add:
1. - Add book
2. - Add DVD\n """)
        if user_option == "1" or user_option == "one":
            books_file = open("books.txt", "a")
            book_name = input("please enter the name of the book")
            author_firstname = input("Please enter the authors first name")
            author_lastname = input("Please enter the authors last name")
            isbn_number = input("Please enter the ISBN number of the book")
            books_file.write(
                f"{book_name}, {author_firstname}, {author_lastname}, {isbn_number}" )
            books_file.close()
        if user_option == "2" or user_option == "two":
            dvd_file = open("dvd.txt", "a")
            dvd_id = input("please enter dvd id ")
            dvd_title = input("Please enter dvd title ")
            year_of_release = input("Please enter the year the dvd was released ")
            rating = input("Please enter dvd rating ")
            duration = input("Pelase enter duration of dvd in mintues")
            genre = input("Please enter genre of dvd")
            dvd_file.write(
                f"{dvd_id}, {dvd_title}, {year_of_release}, {rating}, {genre}, {duration}" )
            dvd_file.close()

    if user_choice == "3" or user_choice == "three":
        user_option = input(
            """\n Please choose what you would like to search for:
1. - Search for book
2. - Search for DVD\n""")
        if user_option == "1" or user_option == "one":
            keyword = input("Please enter keyword ")
            books_file = open("books.txt", "r")
            for row in books_file:
                field = row.split(",")
                book_name = field[0]
                author_firstname = field[1]
                author_lastname = field[2]
                isbn_number = field[3]
                if keyword in book_name:
                    print(book_name, author_firstname, author_lastname,isbn_number)
            books_file.close()
        if user_option == "2" or user_option == "two":
            keyword = input(" please enter keyword ")
            dvd_file = open("dvd.txt", "r")
            for row in dvd_file:
                field = row.split(",")
                dvd_id = field[0]
                title = field[1]
                year_of_release = field[2]
                rating = field[3]
                duration = int(field[4])
                genre = field[5]
                last_char = len(genre) - 1
                genre = genre[0:last_char]
                if keyword in title:
                    print(dvd_id, title, year_of_release, rating, genre,
                          duration)
            dvd_file.close()
    if user_choice == "4" or user_choice == "four":
        print("You have finished")
        break

    else:
        exit = input("\n please press 'y' to continue or 'x' to exit")
        if exit == 'y' or exit == 'yes':
            continue
        else:
            print("You are finished with the program")
            break