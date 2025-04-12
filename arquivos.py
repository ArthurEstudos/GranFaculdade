arquivo = open('pessoas.txt' , 'w')

arquivo.write('joao\n')
arquivo.write('maria\n')
arquivo.write('Arthur\n')

arquivo.close()

with open('pessoas.txt', 'r+') as arquivoleitura:
    for linha in arquivoleitura:
        print(linha)