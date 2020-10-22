def remove_palindroms(spells):
    for i in spells:
        if i == i[::-1]:
            spells.remove(i)
    return spells

