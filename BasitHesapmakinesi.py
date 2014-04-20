import math

sonuc=0
sayi1 = raw_input("sayi giriniz :")
sayi2 = raw_input("sayi giriniz :")

def SonucYazdir():
    print sonuc
def Topla():
    global sonuc
    sonuc=float(sayi1)+float(sayi2)
    SonucYazdir()
def Cikar():
    global sonuc
    sonuc=float(sayi1)-float(sayi2)
    SonucYazdir()    
def Carp():
    global sonuc
    sonuc=float(sayi1)*float(sayi2)
    SonucYazdir()    
def Bol():
    global sonuc
    sonuc=float(sayi1)/float(sayi2)
    SonucYazdir()
def UssuAl():
    global sonuc
    sonuc=math.pow(float(sayi1),float(sayi2))
    SonucYazdir()    
Topla()
Cikar()
Carp()
Bol()
UssuAl()
