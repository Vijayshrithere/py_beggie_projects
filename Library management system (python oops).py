# Functions in the library class:

# 1)display book: It displays all the books in the library along with whether they are available or lent to someone
# 2)lend book: This will allow the user to issue a book from the library. If the requested book is lent to someone
#              then print their name
# 3)add book: This function is used to enter the name of the book to be added to the library
# 4)return book : Allows the user to return a book
#
# The Constructor of the class should take 2 arguments:
# 1) a list of all the book in the library
# 2) the name of the library


class Library:
    def __init__(self,list,name):
        self.booksList = list
        self.name = name
        self.lendDict = { }

    def displayBooks(self):
        print(f"We have following books in a library: {self.name}")
        for book in self.booksList:
            print(book)

    def lendBook(self,user,book):
        if book not in self.lendDict.keys():
             self.lendDict.update({book:user})
             print("Lender-Book database has been updated.You can take your book now")
        else:
            print(f"Book is already being used by {self.lendDict[book]}")

    def addBook(self,book):
        self.booksList.append(book)
        print("Book has been added to the book list")

    def returnBook(self,book):
        self.lendDict.pop(book)
        print("The book has been returned")

if __name__== '__main__':
    Vijayshri = Library(['HTML','Rich Daddy poor Daddy','Harry potter',"c++ Basics"], "Vijayshri's Books")

    while(True):
        print(f"Welcome to the {Vijayshri.name} library. Enter your choice to continue")
        print("1.Display Books")
        print("2.Lend a Books")
        print("3.Add a Books")
        print("4.Return a Books")
        user_choice = input()
        if user_choice not in ['1','2','3','4']:
            print("Please enter a valid option")
            continue

        else:
            user_choice = int(user_choice)

        if user_choice==1:
            Vijayshri.displayBooks()

        elif user_choice==2:
            book = input("Enter the name of the book you want to lend:")
            user = input("Enter your name")
            Vijayshri.lendBook(user,book)


        elif user_choice==3:
            book = input("Enter the name of the book you want to Add:")
            Vijayshri.addBook(book)

        elif user_choice==4:
            book = input("Enter the name of the book you want to return:")
            Vijayshri.returnBook(book)

        else:
            print("Not a valid option")

        print("Press q to quit and c to continue")
        user_choice2 = " "
        while(user_choice2!="c" and user_choice2!="q"):
            user_choice2=input()
            if user_choice2=="q":
                exit()

            if user_choice2=="c":
                continue


