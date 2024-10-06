def powerset_backtracking(input_set):
    def backtrack(start, current_set):
        powerset.append(current_set[:])

        for i in range(start, len(input_set)):
            current_set.append(input_set[i])
            backtrack(i + 1, current_set)
            current_set.pop()

    powerset = []
    backtrack(0, [])
    return powerset