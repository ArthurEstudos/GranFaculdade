import csv

carros = [
    ['VW', 'Virtus', '2017'],
    ['VW', 'Gol', '1999'],
    ['Fiat', 'Palio', '2002'],
]

with open('carros.CSV', 'w', newline='') as arquivo: 
    fileCSV = csv.writer(arquivo, delimiter=";")

    fileCSV.writerow(['Marca', 'Modelo', 'Ano'])
    fileCSV.writerows(carros)
