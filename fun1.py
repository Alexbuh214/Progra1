import os

def cliente():
    Vip = "admin123"
    a = 0
    print("Eres cliente habitual o Vip?")
    print("1. Cliente Habitual")
    print("2. Cliente Vip")
    res = int(input("Dime porfa: "))
    if res == 2:
        n = 0
        while n < 3:
            n += 1
            print("Tienes 3 oportunidades para darme la contraseña del VIP")
            print("Intento número:", n)
            contra = input("Contraseña: ")
            if contra == Vip:
                a = 1
                break
   
    return a
def factura_n():
    n1=120*5
    print("Compraste Playstation 5: $120 ")
    des=n1*0.1
    return des-n1
def factura_v():
    n1=120*5
    print("Compraste Playstation 5: $120 ")
    des=n1*0.1
    return des-n1
    
print("-------------------- TIENDA PINEDA --------------------")
res = cliente()   
os.system("cls")

if res == 1:
    print("felicidades eres vip")
    factura_v()
elif res==0:
    print("Cliente normal")
    factura_n()
