numeros = [4, 8, 9, 3]
'''
resultado = []
for n in numeros:
    resultado.append(n*2)

print(numeros, resultado)

def multiplicar(n1):
    return n1 * 2
'''


resultado = map(lambda n: n * 2, numeros)
print(numeros, list(resultado))