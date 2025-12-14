import string

def count_words(word, text):
    """
    Counts how many times 'word' appears in 'text' as a whole word.
    Ignores capitalization and punctuation at the beginning or end.
    """
    word = word.lower()
    text = text.lower()
    words = text.split()
    count = 0
    for w in words:
        cleaned = w.strip(string.punctuation)
        if cleaned == word:
            count += 1
    return count

print(count_words("ban", "ban is banana"))          # Expected: 1
print(count_words("apple", "Apple, apple! APPLE.")) # Expected: 3
print(count_words("dog", "A dog, the Dog; and doggo.")) # Expected: 2
print(count_words("tree", "Tree. tree! tree?"))     # Expected: 3
print(count_words("sun", "The sunshine is bright.")) # Expected: 0
