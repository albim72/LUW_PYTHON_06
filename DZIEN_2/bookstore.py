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
        self.newbook()

    def __repr__(self):
        return f"{self.title} by {self.author}, binding: {self.binding}, price: {self.price}, bookstore_nb: {self.bookstore_nb}"
    #zachowanie

    def newbook(self):
        print("Nowy obiekt klasy Book!")

    def get_binding(self):
        return self.binding

    def set_binding(self,binding):
        self.binding = binding

    def cena_rabat(self,procent):
        self.price = self.price - self.price * procent/100
        return self.price

    def obwoluta(self):
        return self.__kolor


if __name__ == '__main__':
    b1 = Book("ABC ultra biegacza","Marcin Świerc",102,345,22)
    print(b1)
    print(b1.binding) # zła praktyka
    print(b1._grubosc)
    # print(b1.__kolor)
    b1.price = 99 # bardzo zła praktyka
    print(b1)
    print(b1.__class__.__name__)

    print(b1.get_binding())
    b1.set_binding("twarda")
    print(b1.get_binding())
    print(f"cena po rabacie 6% : {b1.cena_rabat(6)} zł")
    print(f"kolor obowluty: {b1.obwoluta()}")

