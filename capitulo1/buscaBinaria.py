'''
    @Autora: @letyresinaa
    Capítulo 1: introdução aos algoritmos - Busca binária
    --------------------------------------------------------------------------------------------------
    Busca binária é um algoritmo que busca um elemento numa lista ordenada eliminando pelas metades
    até que reste o gatilho principal para que o algoritmo retorne a posição em que esse elemento está,
    caso contrário, retorna None.

    Importante ressaltar que a busca binária funciona com log n elementos com a base 2. Como exemplo, 
    em uma lista de 1.024 elementos, terá que passar no máximo por 10 etapas para encontrar o elemento 
    de busca.
'''

# criando a função de busca binária
def pesquisa_binaria(lista, item):
    """
        A função tem como objetivo principal pegar um array (lista) ordenado e um item que chamaremos de
        elemento de busca. Caso esse elemento está dentro do array, ele retornará a posição em que está
    """
    # acompanhando a parte em que estou procurando a lista
    baixo = 0
    alto = len(lista) - 1 

    # looping para enquanto não chegar em um único elemento
    while baixo <= alto:
        meio = (baixo + alto) // 2 # busca qual o elemento do meio através da posição dele
        chute = lista[meio]
        if chute == item: # se encontrar o elemento de busca
            return meio # retorna então a posição em que ele está
        if chute > item:
            alto = meio - 1 # o chute foi muito alto do elemento de busca
        else:
            baixo = meio + 1 # o chute foi muito baixo do elemento de busca
    return None # caso não encontre o elemento

# criando uma lista para testar
lista = [1, 3, 5, 7, 9]

# testando então a busca das posições 
print(pesquisa_binaria(lista, 3)) # precisa retornar 1
print(pesquisa_binaria(lista, 9)) # precisa retornar 4
print(pesquisa_binaria(lista, -1)) # precisa retornar None