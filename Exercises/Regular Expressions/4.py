import re

def extract_emails(text):
    pattern = r'\b[\w\.-]+@[\w\.-]+\b'

    emails = re.findall(pattern, text)
    return emails

text = input()

extracted_emails = extract_emails(text)

for email in extracted_emails:
    print(email)
