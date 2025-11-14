def up_to_period(filename):
    file_in = open(filename, 'r')
    all_the_rest = file_in.read()
    new_string = ""
    for ch in all_the_rest:
        new_string = new_string + ch
        if ch == '.':
            break
    file_in.close()
    return new_string

print(up_to_period('../TextFiles/mockingbird.txt'))

