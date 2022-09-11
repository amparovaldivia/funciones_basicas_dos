


def cuenta_regresiva(numero):
    x=[]
    for valor in range(numero,-1,-1):
        x.append(valor)
    return x  
y=cuenta_regresiva(7)
print(y)

def imprimir_devolver (numero):
    print(numero[0])
    return numero[1]
y=imprimir_devolver([3,4])
print(y)  


def lista(numero):
    x=len(numero)+numero[0]
    return x
y=lista([1,2,3,4,5,6]) 
print(y)   


def crear_lista(numeros):
    if len(numeros)<=2:
        return False
    x=[]    
    for numero in numeros:
        if numero>numeros[1]:
            x.append(numero)
    return x
y=crear_lista([3,2,5,6,9])
print(y)       

def crear_lista_dos(tamano,valor):
    x=[]
    for i in range(tamano):
        x.append(valor)
    return x
y=crear_lista_dos(4,2)
print(y)