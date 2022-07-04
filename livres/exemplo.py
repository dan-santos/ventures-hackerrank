from random import sample

if __name__ == '__main__':
  lista = [10, 4, 6, 88, -2, 3]
  lista.sort()
  print(sample(lista, 3))