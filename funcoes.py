def somar(n1, n2):
    return n1 + n2

def Subtrair(n1, n2):
    return n1 - n2

def multiplicar(n1, n2):
    return n1 * n2
    

def dividir(n1, n2):
    if n2 == 0:
        print("não é possivel dividir um numero por zero")
    else:
        resultado = n1 / n2 
        #print(f'{n1} / {n2} = {resultado}')
        return resultado

def calcular(n1, n2, operador):
    match operador:
        case '+': return somar (n1, n2)
        case '*': return multiplicar (n1, n2)
        case '-': return Subtrair (n1, n2)
        case '/': return dividir (n1, n2)
        case other: return 'Operador não encontrado'

print(calcular(5, 10, '+'))
print(calcular(5, 10, '*'))
print(calcular(5, 10, '-'))
print(calcular(5, 18, '/'))
print(calcular(5, 18, 'o'))


#divisao = dividir(10, 2)
#print("o resultado da divisão é", divisao)

#print("o resultado é", dividir(80, 50))

#resultado = dividir(283, 10) 
#soma = 20 + resultado
#print("a soma é", soma)

#print("o resultado foi: " , dividir(10, 5))