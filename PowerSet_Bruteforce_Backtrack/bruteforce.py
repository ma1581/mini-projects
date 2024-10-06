def powerset_bruteforce(input_set):
    n = len(input_set)
    powerset = []

    for i in range(2 ** n):
        subset = []
        for j in range(n):
            if (i >> j) & 1:
                subset.append(input_set[j])
        powerset.append(subset)

    return powerset