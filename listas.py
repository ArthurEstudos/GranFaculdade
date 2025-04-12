numeros = [10, 20, 30, 17, 58, 3, 7]
print(numeros[0])

carros = ['palio', 'virtus', 'polo', 'ka', 'onix']
print('1 ->', carros)

carros.append('kombi')
print('2 ->', carros)

carros.remove('palio')
print('3 ->', carros) 

del carros [4]
print('4 ->', carros)

carros = sorted(carros)
print('5 ->', carros)

for i in (carros):
    print(i) 