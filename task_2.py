from collections import Counter


def count_elements(list_version):
    counts = Counter(tuple(elem) for elem in list_version)
    result = [[elem[0], elem[1], count] for elem, count in counts.items()]
    return result


list_version = [['665587', 2], ['669532', 1], ['669537', 2], ['669532', 1], ['665587', 1]]

result = count_elements(list_version)
print(result)
