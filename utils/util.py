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

def read_lines(path_to_file):
    with open(path_to_file, 'r') as file_object:
        return [x.strip() for x in file_object.readlines()]