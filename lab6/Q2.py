def insert_items(s, before, after):
    i = 0
    while i < len(s):
        if s[i] == before:
            s.insert(i + 1, after)
            i += 1
        i += 1
    return s
