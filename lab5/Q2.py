def berry_finder(t):
    if label(t) == 'berry':
        return True
    for branch in branches(t):
        if berry_finder(branch):
            return True
    return False
