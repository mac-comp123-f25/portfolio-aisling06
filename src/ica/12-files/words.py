def i_words(filename):
    file_in = open(filename, 'r')
    allFile = file_in.read()
    file_in.close()
    words = allFile.split()
    new_list = []
    for word in words:
        if 'i' in word:
            new_list.append(word)
    return new_list
print(i_words("../TextFiles/alice.txt"))



