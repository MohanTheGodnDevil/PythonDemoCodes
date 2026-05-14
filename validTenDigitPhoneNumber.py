import re

text = "Call 9876543210 or 987-654-3210. Alternate: (91234 56780)"

# Regex patterns
patterns = [
    r'\b\d{10}\b',                  # 9876543210
    r'\b\d{3}-\d{3}-\d{4}\b',      # 987-654-3210
    r'\(\d{5}\s\d{5}\)'            # (91234 56780)
]

numbers = []

for pattern in patterns:
    matches = re.findall(pattern, text)

    for match in matches:
        # Remove non-digit characters
        clean_num = re.sub(r'\D', '', match)

        if len(clean_num) == 10 and clean_num not in numbers:
            numbers.append(clean_num)

# Create dictionary
result = {num[-4:]: num for num in numbers}

print(result)
