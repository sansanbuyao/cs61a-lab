def merge(lst1, lst2):
    if len(lst1) == 0:
        return lst2
    if len(lst2) == 0:
        return lst1
    
    merged = []
    i = j = 0
    
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            merged.append(lst1[i])
            i += 1
        else:
            merged.append(lst2[j])
            j += 1
    
    if i < len(lst1):
        merged.extend(lst1[i:])
    
    if j < len(lst2):
        merged.extend(lst2[j:])
    
    return merged
