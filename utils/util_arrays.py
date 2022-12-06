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

def splt_into_groups(group_size, data):
    results = []
    results.append([])
    idx = 0
    for item in data:
        results[-1].append(item)
        idx += 1
        if idx == group_size:
            results.append([])
            idx = 0
    return results

