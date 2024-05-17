'''
    @Autora: @letyresinaa
    Capítulo 2: Ordenação por seleção - Quicksort
    --------------------------------------------------------------------------------------------------
    Nesse capítulo, entendemos a diferença entre lista e array. E, portanto, pegando um link do capítulo
    anterior, ordenação e como funciona a memória de um computador.

    Foi citado, de forma resumida, a notação Big O. E, como exemplo de código, foi ensinado o então
    Quicksort, um algoritmo eficiente de ordenação.
'''

# função que encontra o menor número em um array
def buscaMenor(arr):
    """
        A função começa partindo do pressuposto que o menor valor é o valor que está contido no primeiro
        índice (0), e que, consequentemente, o índice é 0. Depois, em uma estrutura de repetição, ela
        então começa a pesquisar valor por valor dentro do array para descobrir se esse é menor que o
        anteriormente informado. Caso sim, ele armazena então o valor na variável menor, e retorna o índice
        em que esse valor está.
    """
    menor = arr[0] 
    menor_indice = 0 
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice

# função de ordenação
def ordenacaoSelecao(arr):
    """
        A função inicia criando um array vazio, e logo após, uma estrutura de repetição que,
        vai buscando dentro do array anteriormente informado o menor valor (com a função criada
        anteriormente), e assim, vai adicionando nesse novo array. Quando ele encontra então o menor
        array, ele tira o espaço previamente dado para o antes menor e em seguida, adiciona o valor novo
    """
    novoArr = []
    for i in range(len(arr)):
        menor = buscaMenor(arr)
        novoArr.append(arr.pop(menor))
    return novoArr

# lista criada
arr = [5, 3, 6, 2, 10]

# prints
print(ordenacaoSelecao(arr)) # retorna então a nova lista ordenada