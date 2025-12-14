def print_abbrev(filename):
    file_in = open(filename, 'r')

    for line in file_in:
        short_line = line[:20]
        print(short_line)

    file_in.close()

print_abbrev('../TextFiles/alice.txt')