def valorDeN(n):
  for i in range(n):
    print("\r")
    for i in range(i+1):
      print(str(i + 1), end=" ")
      
n = int(input("Valor de N:"))
valorDeN(n)