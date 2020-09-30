def su():
  print("Ingrese un número")
  a=int(input())
  print("Ingrese un número")
  b=int(input())
  c=a+b
  print("La suma es "+str(c))

def res():
  print("Ingrese un número")
  a=int(input())
  print("Ingrese un número")
  b=int(input())
  c=a-b
  print("La resta es "+str(c))

def pro():
  print("Ingrese un número")
  a=int(input())
  print("Ingrese un número")
  b=int(input())
  c=a*b
  print("El producto es "+str(c))
  
def div():
  print("Ingrese un número")
  a=int(input())
  print("Ingrese un número")
  b=int(input())
  if b <= 0:
    while b<=0:
      b=int(input())
  c=a/b
  print("La división es "+str(c))