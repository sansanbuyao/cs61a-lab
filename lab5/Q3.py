def replace_loki_at_leaf(t, lokis_replacement):
    if is_leaf(t):
        if label(t) == 'loki':
            return tree(lokis_replacement)
        else:
            return t
    else:
        new_branches = [replace_loki_at_leaf(branch, lokis_replacement) for branch in branches(t)]
        return tree(label(t), new_branches)
