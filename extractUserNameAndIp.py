import re

log = """
User: alice IP: 192.168.1.10  
User: bob IP: 10.0.0.2  
User: alice IP: 192.168.1.11  
User: bob IP: 10.0.0.2
"""

# Regex pattern
pattern = r"User:\s*(\w+)\s*IP:\s*([\d\.]+)"

matches = re.findall(pattern, log)

result = {}

for user, ip in matches:
    if user not in result:
        result[user] = []

    if ip not in result[user]:
        result[user].append(ip)

print(result)

