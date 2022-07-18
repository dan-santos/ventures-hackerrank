from random import sample

"""
Buscar por um valor dado numa lista aleatória e retornar o índice desse valor na lista, caso exista.
input -> valor: int
output -> indice: int

8 min
piloto -> codar
co-piloto -> ajudar o piloto
galera 
https://media.geeksforgeeks.org/wp-content/uploads/20220309171621/BinarySearch.png
"""
def buscar_indice_binaria_recursiva(valor_buscado: int, lista: list) -> int:
    
    inicio=0
    fim=len(lista)-1
    meio=(inicio+fim)//2
    if meio < 0:
        return -1
    if lista[meio]==valor_buscado:
        return meio
    elif valor_buscado < lista[meio]:
        fim=meio-1
        return buscar_indice_binaria_recursiva(valor_buscado, lista[0:fim])
    elif valor_buscado > lista[meio]:
        inicio=meio+1
        return buscar_indice_binaria_recursiva(valor_buscado, lista[inicio:fim])

"""
O (log n) <- complexidade de tempo
O (1) <- complexidade de espaço
"""
def buscar_indice_binaria_iterativa(valor_buscado: int, lista: list) -> int:
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        if valor_buscado > lista[meio]:
            inicio = meio + 1
        elif valor_buscado == lista[meio]:
            return meio
        else:
            fim = meio - 1
    
    return -1


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
lista = sample(lista, 50)

lista1 = sorted(lista)

print(lista1)


valor_buscado = int(input('Valor para buscar na lista: '))

#print(f' (l) O valor {valor_buscado} está presente na lista no índice {buscar_indice_linear(valor_buscado, lista)}.')
print(f' (b) O valor {valor_buscado} está presente na lista no índice {buscar_indice_binaria_recursiva(valor_buscado, lista1)}.')
