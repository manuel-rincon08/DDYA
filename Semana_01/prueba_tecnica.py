
serie = []
def positivo (num):
    if num < 0:
        return('numero negativo')
    elif num > 0:
        return('numero positivo')
    else:
        return('es cero')
def par_impar(num):
    if num % 2 == 0:
        return('Es un número par')
    else:
        return('Es un número impar')
def fibonacci(num):
    a = 0
    b = 1
    for i in range(num):
        if a <= num:
            serie.append(a) 
        c = a+b
        a =b
        b =c
        
            
            
    return serie


def ingresar():
    print('Ingrese un numero')
    num = int(input())
    return num

def primo (num):
    impar = 0
    for i in range (1,num):
        if num //i == 0:
            impar +=1
    if impar == 2:
        return ('es primo')
    else:
        return('No es primo')

def sumar(num,num2):
    if num < num2:
        a = num2
        b = num
    else:
        a = num
        b = num2
    sum = 0
    for i in range (b,a-1):
        sum += i+1
    intermedios = sum
    return intermedios

def vocales_consonantes(mes):


def main ():
    num = ingresar()
    signo = positivo(num)
    par = par_impar(num)
    serie = fibonacci (num)
    prim = primo(num)
    print(num)
    print(signo)
    print(par)
    print(serie)
    print(prim)
    num2 = ingresar()
    signo = positivo(num2)
    par = par_impar(num2)
    serie = fibonacci (num2)
    prim = primo(num2)
    print(num)
    print(signo)
    print(par)
    print(serie)
    print(prim)

    intermedios = sumar(num,num2)  
    print(intermedios)
    if intermedios%2 == 0:
        intermedios = intermedios **3
    else:
        intermedios = intermedios **2
    print(intermedios)
    codigo = int(input('Ingrese su codigo de estudiante'))
    signo = positivo(codigo)
    par = par_impar(codigo)
    serie = fibonacci (codigo)
    prim = primo(codigo)
    print(codigo)
    print(signo)
    print(par)
    print(serie)
    print(prim)
    nacimiento = int(input('diga su fecha de nacimiento, con su codigo'))
    # lo hubiera separado las letras con los números haber hecho que el sistema cuando vea la primera letra guarde eso y cuando empiece el numero deje de guardar

    ## con if puedo sacar cuales son vocales haciendo antes un split y luego un for 

    ### seria hacer una lista con el abecedario y luego ubicar cada letra donde pertenece para saber la posición y le sumo uno al mostrarlo 








main()





