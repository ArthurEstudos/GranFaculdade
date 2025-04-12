continuar = True

while continuar:

    numero = int(input("qual tabuada?"))
    for i in range(1, 11):
         print(f"5{numero} x {i} = {numero*i}") 
    
    continuar = input('deseja continuar? (s/n)')
    continuar = True if continuar == 's' else False

    #while i < 11:
    #print(f"2 x {i} = {2*i}")
    #i = i + 1
    #i += 1 
