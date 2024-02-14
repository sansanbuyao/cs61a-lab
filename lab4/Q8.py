def count_palindromes(L):
    count = 0
    for word in L:
        if word.lower() == word.lower()[::-1]:
            count += 1
    return count
