def my_reduce(combiner, seq):
    result = seq[0]
    for i in range(1, len(seq)):
        result = combiner(result, seq[i])
    return result
