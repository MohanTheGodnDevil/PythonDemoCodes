import re

log = """
[2025-10-05] User: alice Action: login
[2025-10-05] User: bob Action: upload
[2025-10-06] User: alice Action: logout
"""

pattern = r"\[(.*?)\]\s*User:\s*(\w+)\s*Action:\s*(\w+)"

matches = re.findall(pattern, log)

result = {}

for date, user, action in matches:
    if user not in result:
        result[user] = {}

    result[user][date] = action

print(result)
