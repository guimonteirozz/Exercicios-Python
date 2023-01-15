def valorDeN(n):
  for i in range(n): # repete a linhas ate a n-enésima linha
    print("\r")
    for i in range(i+1):
      print(str(i + 1), end=" ") # Imprimi os numeros ate o valor de i + 1 em linha reta
      
n = int(input("Valor de N: "))
valorDeN(n)

'''
  1
  1   2
  1   2   3
  .....
  1   2   3   ...  n
'''