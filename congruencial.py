#congruencial lineal
def congruencial(x0, a, b, m):
    return (a * x0 + b) % m;
n = int(input('Ingrese la cantidad de números a generar: '))
x = int(input("Introduce el valor de la semilla: "))

c = int(input("Introduce el valor de la constante aditiva: "))
g = int(input("Introduce el valor del periodo: "))
k = int(input("Introduce el valor de k: "))
a = 1 + (4*k)
m = 2**g
ini = x
cont = 0
for i in range(n):
    x = congruencial(x, a, c, m);
    r = x/(m-1)
    print(r)
    if ini != x:
        cont += 1

print("contador", cont)
if m == cont:
    print("es completo")
else:
    print("es incompleto")