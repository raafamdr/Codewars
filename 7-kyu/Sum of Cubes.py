def sum_cubes(n):
    soma = 0
    for i in range(n+1):
        soma += pow(i, 3)
    return soma
