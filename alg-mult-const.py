X = list()
Y = list()
i = 0
D = list()
s = int(input('Introduzca el valor de la semilla: '))
n = int(input('Introduzca la cantidad de números a generar: '))
a = int(input('Introduzca el valor de la constante: '))

X.insert(0, s)
print (X[0])
while i < n:

for i in range(n):
    print(i)
    if i >= 1 and i < n-1:
        D.insert = str((X[i-1]*a)[2:6])
        X.insert(i, D[i])
        print('X' + str(i) + ' = ' + str(X[i]))