uno = 0.0
dos = 0
op = ""
res = 0.0


print("Hola, Bienvenido!")
uno = float(input("Ingresa un número: "))
dos = float(input("Ingresa otro número: "))
op = input("Ingresa la operación (+, -, *, /): ")

if op == "+":
    res = uno + dos
elif op == "-":
    res = uno - dos
elif op == "*":
    res = uno * dos
elif op == "/":
    if dos != 0:
        res = uno / dos
    else:
        print("Error: División por cero")
else:
    print("Operación no válida")

print(f"El resultado de {uno} {op} {dos} es {res}")

#GREAT
#Hola como vas, hace tiempo no se de ti

#MARCOS ERES GEI
# si, soy gei


