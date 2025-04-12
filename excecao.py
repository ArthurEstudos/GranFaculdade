try:
    n1 = int(input('numero 1: '))
    n2 = int(input('numero 2: '))
    resultado = n1 / n2 
    print(f"o resultado da divisão foi: {resultado}")

except Exception as erro:
    print(f"ocorreu um erro: {erro}")

except ValueError:
    print("favor digitar somente números")

except ZeroDivisionError:
    print("Não é possivel dividir um numero por 0")

else:
    print("O programa foi executado corretamente")

finally:
    print("Fim!!!")
    