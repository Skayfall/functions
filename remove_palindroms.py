def remove_palindroms(spells):
    lst = [i for i in spells]
    for i in lst:
        if i.lower().replace(' ', '') == i.lower()[::-1].replace(' ', ''):
            spells.remove(i)
    return spells
