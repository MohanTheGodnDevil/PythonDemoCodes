# Extract email addresses and store domain names in dictionary

import re

text = "Contact us at support@example.com or sales@company.org for more info."

# Regular expression for emails
emails = re.findall(r'[\w\.-]+@[\w\.-]+', text)

email_dict = {}

for email in emails:
    domain = email.split("@")[1]
    email_dict[email] = domain

print(email_dict)