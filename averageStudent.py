text = "Alice: 89, Bob: 76, Charlie: 92, Alice: 95, Bob: 82"

entries = text.split(", ")

marks = {}

for entry in entries:
    name, score = entry.split(": ")
    score = int(score)

    if name not in marks:
        marks[name] = []

    marks[name].append(score)

# Calculate averages
average_marks = {}

for name, scores in marks.items():
    average_marks[name] = sum(scores) / len(scores)

print(average_marks)
