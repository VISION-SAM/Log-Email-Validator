import re
import sys
import os
from email_validator import validate_email, EmailNotValidError

pattern = r'\b[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-+]+(?:\.[a-zA-Z-]+)+\b'

if len(sys.argv)<2:
    print("Usage : python emailextractor.py <location>")
    sys.exit(1)

folder_path = sys.argv[1]

email_list = set()
valid_emails = set()
cache = ()

for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith(('.log', '.txt')):
            full_path = os.path.join(root, file)

            try:
                with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
                    for line in f:
                   #     if 'email' in line.lower() or 'from' in line.lower() or 'emails' in line.lower():
                        emails = re.findall(pattern, line)

                        for email in emails:
                            email = email.lower()
                            email_list.add(email)

                            try:
                                v = validate_email(email,check_deliverability=True)
                                valid_emails.add(v.normalized)
                                print(f'[✅ VALID] {full_path} : {email.strip()}')
                            except EmailNotValidError as e:
                                print(f'[❌ INVALID] {full_path} : {email} : {e}')

            except Exception as e:
                print(f'Unable to read file {full_path} : {e}')

print(f"Total Emails = {len(email_list)}")
print(f"Total Valid Emails = {len(valid_emails)}")
