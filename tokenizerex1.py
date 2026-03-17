text = input("Enter a sentence: ")

clean_text = text.lower()
punctuation = ",.!?;:\"'()[]{}"

for p in punctuation:
    clean_text = clean_text.replace(p, "")

words = clean_text.split()

freq = {}

for w in words:
    if w in freq:
        freq[w] += 1
    else:
        freq[w] = 1

print("word frequency:\n")
for word, count in freq.items():
    print(f"{word}: {count}")
