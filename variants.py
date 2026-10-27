"""Two approaches to the same task: find duplicate values in a list.

naive_duplicates:     O(n^2) nested loops  -> more CPU time -> more energy
efficient_duplicates: O(n) using a set     -> less CPU time -> less energy
"""


def naive_duplicates(items):
    dups = []
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i] == items[j] and items[i] not in dups:
                dups.append(items[i])
    return dups


def efficient_duplicates(items):
    seen, dups = set(), set()
    for x in items:
        if x in seen:
            dups.add(x)
        else:
            seen.add(x)
    return list(dups)
