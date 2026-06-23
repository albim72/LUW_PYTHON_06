from opis import policz

class Kalkulator:
    def __init__(self,x:int,y:int,z:int,k:int,h:int):
        self.x = x
        self.y = y
        self.z = z
        self.k = k
        self.h = h
        
    def wartA(self):
        return (self.k+self.h)/2
    
    def wartB(self):
        return policz(self.k,self.z,self.x)+self.y*self.h
