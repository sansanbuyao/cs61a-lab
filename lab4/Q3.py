def my_filter(pred, seq):
    return [x for x in seq if pred(x)]
