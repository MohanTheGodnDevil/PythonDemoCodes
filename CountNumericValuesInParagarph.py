# Count numeric values in a paragraph using regex

import re

text = "I bought 3 apples, 4.5 kg of mangoes, and 3 more oranges. Total: 7.5 kg."

# Regex to find integers and decimal numbers
numbers = re.findall(r'\d+\.\d+|\d+', text)

number_count = {}

for num in numbers:
    if num in number_count:
        number_count[num] += 1
    else:
        number_count[num] = 1

print(number_count)