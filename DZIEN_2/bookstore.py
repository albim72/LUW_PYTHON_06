class Book:
    #predefinicje
    __kolor = "czerwony" # __ - private
    _grubosc = 3 # _ - protected

    #stan - konstuktory
    def __init__(self,title,author,price,pages,bookstore_nb):
        self.title = title
        self.author = author
        self.price = price
        self.bookstore_nb = bookstore_nb
        self.pages = pages
        self.binding = "miękka"
    #zachowanie
