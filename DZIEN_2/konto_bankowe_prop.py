class KontoBankowe:
    def __init__(self,wlasciciel:str, saldo:float=0.0):
        self._wlasciciel = wlasciciel
        self._saldo = saldo
        
    @property
    def wlasciciel(self):
        return self._wlasciciel
    
    @wlasciciel.setter
    def wlasciciel(self,wlasciciel):
        self._wlasciciel = wlasciciel
        
    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self,kwota:float):
        if kwota < 0:
            raise ValueError("kwota nie może być ujemna!")
        self._saldo = kwota
        
    @saldo.deleter
    def saldo(self):
        print("saldo zostało wyzerowane....")
        self._saldo = 0.0


if __name__ == '__main__':
    konto = KontoBankowe('Jakub')
    print(konto)
