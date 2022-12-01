def group_by_blanks(data):
    results = [[]]
    for x in data:
        if x  != "":
            results[-1].append(x)
        else:
            results.append([])
    return results

def strs_to_ints(data):
    return [int(x) for x in data]

