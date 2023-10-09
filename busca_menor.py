def buscaMenor(arr):
    menor = arr[0]
    menor_indice = 0

    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor_indice = i
    
    return menor_indice

def ordenacaoSelecao(arr):
    novoArr = []

    for i in range(len(arr)):
        menor = buscaMenor(arr)
        novoArr.append(arr.pop(menor)) # adiciona no novo array e tira do antigo

    return novoArr

print(ordenacaoSelecao([5, 3, 6, 2, 10]))
