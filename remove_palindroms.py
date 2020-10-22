def remove_palindroms(spells):
    for i in spells:
        if i.lower() == i.lower()[::-1]:
            spells.remove(i)
    return spells
