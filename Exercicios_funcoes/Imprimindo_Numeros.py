def valorDeN(n):
  for i in range(n):
    i_mais_1 = i + 1 
    print(str(str(i_mais_1) + " ") * i_mais_1)

n = int(input("Valor de N: "))
valorDeN(n)

'''
Faça um programa para imprimir:
    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n

'''
