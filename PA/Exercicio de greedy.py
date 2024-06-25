def largest_minimum(n, a, queries):
    results = []
    
    # Encontrar o maior elemento do array
    max_element = max(a)
    
    # Para cada consulta, determinar o maior mínimo possível
    for k in queries:
        min_value = max_element + k
        
        # Verificar se o número de operações é par ou ímpar
        if k % 2 == 0:
            results.append(min_value)
        else:
            results.append(min_value + 1)
    
    return results

# Ler a entrada
n, q = map(int, input().split())
a = list(map(int, input().split()))
queries = list(map(int, input().split()))

# Chamar a função e imprimir o resultado
result = largest_minimum(n, a, queries)
print(*result)
