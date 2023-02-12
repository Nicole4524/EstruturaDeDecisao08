#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato

preco1 = float(input("Informe o valor do primeiro produto:"))
preco2 = float(input("Informe o valor do segundo produto:"))
preco3 = float(input("Informe o valor do terceiro produto:"))

if preco1 < preco2 and preco1 < preco3:
    print("O produto mais barato é o:", preco1)
elif preço2 < preco1 and preco2 < preco3:
    print("O produto mais barato é o:", preco2)
elif preço3 < preco2 and preco3 < preco1:
    print("O produto mais barato é o:", preco3)
