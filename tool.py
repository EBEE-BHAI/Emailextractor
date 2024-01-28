import requests
from bs4 import BeautifulSoup
import re

def extract_emails(website_url):
    try:
        response = requests.get(website_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find email addresses using a regular expression
        emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', soup.get_text())

        return emails
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Example usage
website_url = "https://www.marham.pk/contact"  # Replace with the actual website URL
extracted_emails = extract_emails(website_url)

print("Extracted Email Addresses:")
for email in extracted_emails:
    print(email)
