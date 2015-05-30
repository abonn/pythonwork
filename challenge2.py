def del_dups(seq):
    seen = {}
    pos = 0
    for item in seq:
        if item not in seen:
            seen[item] = True
            seq[pos] = item
            pos += 1
    del seq[pos:]

lst = [8, 8, 9, 9, 7, 15, 15, 2, 20, 13, 2, 24, 6, 11, 7, 12, 4, 10, 18, 
       13, 23, 11, 3, 11, 12, 10, 4, 5, 4, 22, 6, 3, 19, 14, 21, 11, 1, 
       5, 14, 8, 0, 1, 16, 5, 10, 13, 17, 1, 16, 17, 12, 6, 10, 0, 3, 9, 
       9, 3, 7, 7, 6, 6, 7, 5, 14, 18, 12, 19, 2, 8, 9, 0, 8, 4, 5]
del_dups(lst)
print(lst)