def menorNumero(arr):
    menor = arr[0]
    menor_indice = 0

    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice

def listaOrdenar(arr):
    novoArr = []

    for i in range(len(arr)):
        menor = menorNumero(arr)
        novoArr.append(arr.pop(menor))
    return novoArr

print(listaOrdenar([1, 135, 200, 20, 530, 10, 720, 1000]))

def listaOrdenar(arr):
    total = 0
    for x in arr:
        total += x
    return total

print(listaOrdenar([1, 135, 200, 20, 530, 10, 720, 1000]))