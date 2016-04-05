def permutation(s):
    if len(s) ==1:
        return [s]

    perm_list = []
    for a in s:
        remaining_elements = [x for x in s if x != a]
        z = permutation(remaining_elements)

        for t in z:
            perm_list.append([a] + t)
    return perm_list

print str(permutation('ABC'))
