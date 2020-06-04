def triangular_series(n):
    j = 2
    k = 2
    list=[]
    # For each iteration increase j
    # by 1 and add it into k
    for i in range(1, n + 1):
        list.append(k)
        j = j + 1  # Increasing j by 1
        # Add value of j into k and update k
        k = k + j
    print(list)
n = 20
triangular_series(n)
