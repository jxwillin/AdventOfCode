def read_lines(path_to_file):
    with open(path_to_file, 'r') as file_object:
        return [x.strip() for x in file_object.readlines()]