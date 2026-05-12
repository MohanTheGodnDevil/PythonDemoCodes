# Find capitalized words and count occurrences

text = "Alice met Bob . Alice and Bob went to Paris. Bob liked Paris."

# Remove punctuation
text = text.replace(".", "")

words = text.split()

capital_words = {}

for word in words:
    # Check if word starts with a capital letter
    if word.istitle():
        if word in capital_words:
            capital_words[word] += 1
        else:
            capital_words[word] = 1

print(capital_words)