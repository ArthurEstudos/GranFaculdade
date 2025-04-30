class produto:

    def __init__(self, nome, marca, quantidade, modelo, valor):
        self.nome = nome
        self.marca = marca
        self.quantidade = quantidade
        self.modelo = modelo
        self.valor = valor

    def vender(self, quantidade):
        if(quantidade > self.quantidade):
            print('**************************************')
            print('Não há estoque suficiente!')
            print('Quantidade máxima:', self.quantidade)
            print('**************************************')
        else:
            self.quantidade -= quantidade

    def comprar(self, quantidade):
        self.quantidade += quantidade

    

produto0 = produto('celular', 'Apple', 100, 'iphone 14', 5000)
produto0.comprar(100)
produto0.vender(110)

produto1 = produto('Geladeira', 'brastemp', 55, 'SmartFreezer', 7000)
produto1.comprar(18)
produto1.vender(10)

produto2 = produto('notebook', 'lenovo', 76, 'Gamer', 8500)
produto2.comprar(20)
produto2.vender(12)

print(produto0.__dict__)
print(produto1.__dict__)
print(produto2.__dict__)