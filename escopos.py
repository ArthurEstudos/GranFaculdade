#numeros Globais, servem para todo o código!

n1 = 10
n2 = 10
n3 = 10
n4 = 10

#função!
def soma(n1, n2, n3, n4):
    print('Função soma n1:', n1)
    print('Função soma n2:', n2)
    print('Função soma n3:', n3)
    print('Função soma n4:', n4)

soma(5, 8, 90, 70)

#vai pegar os numeros fora da função! (Globais)
print('n1:', n1)
print('n2:', n2)
print('n3:', n3)
print('n4:', n4)