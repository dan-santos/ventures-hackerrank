from random import shuffle

"""
Buscar por um valor dado numa lista aleatória e retornar o índice desse valor na lista, caso exista.
input -> valor: int
output -> indice: int
"""


"""
O (?)
"""
def buscar_indice_binaria(valor_buscado: int, lista: list) -> int:
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        if valor_buscado > lista[meio]:
            inicio = meio + 1


"""
O (n) <- complexidade de tempo
O (1) <- complexidade de espaço

"""
def buscar_indice_linear(valor_buscado: int, lista: list) -> int:
    for i in range(len(lista)):
        if lista[i] == valor_buscado:
            return i
    return -1
    


lista =  list(range(1000))

sorted(lista)
print(lista)

valor_buscado = int(input('Valor para buscar na lista: '))

print(f' (l) O valor {valor_buscado} está presente na lista no índice {buscar_indice_linear(valor_buscado, lista)}.')
print(f' (b) O valor {valor_buscado} está presente na lista no índice {buscar_indice_binaria(valor_buscado, lista)}.')
