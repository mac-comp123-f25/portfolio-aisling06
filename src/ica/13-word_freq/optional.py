def print_frequencies_sorted(freq_dict):
    freq_list = []
    for word, freq in freq_dict.items():
        freq_list.append((freq, word))

    freq_list.sort(reverse=True)

    print("Word".ljust(20), "Frequency")
    print("-" * 30)

    for freq, word in freq_list:
        print(word.ljust(20), freq)
