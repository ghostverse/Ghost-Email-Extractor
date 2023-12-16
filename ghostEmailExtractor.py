# ghostEmailExtractor - version 1.6
# For tools contact me: https://t.me/ghostverse
import pandas as pd
import os
import re
import logging

# Configure logging to save errors to a file
logging.basicConfig(filename='error.txt', level=logging.ERROR)

# ANSI color codes for console output
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
BLUE = '\033[94m'
RESET = '\033[0m'

def clean_email(email):
    # Remove extra spaces, quotes, and unwanted characters
    email = email.strip().replace('"', '').replace(' ', '').replace('""""', '').replace('"', '')
    email_parts = email.split(',')
    # Keep only the email part (before the first comma)
    return email_parts[0]

def extract_emails_from_file(input_file, output_file, domain_extensions=None, exclude_emails=None):
    if not os.path.exists(input_file):
        error_message = f"Error: The input file '{input_file}' does not exist."
        logging.error(error_message)
        print(RED + error_message + RESET)
        return

    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # Use regular expression to find email-like patterns in the content
    email_pattern = r'\S+@\S+'
    extracted_emails = re.findall(email_pattern, content)

    if not extracted_emails:
        error_message = "No email addresses found in the input file."
        logging.error(error_message)
        print(YELLOW + error_message + RESET)
        return

    # Create a DataFrame from the extracted emails
    df = pd.DataFrame({'emails': extracted_emails})

    # Optionally filter emails by domain extensions
    if domain_extensions:
        extensions = [ext.strip().lower() for ext in domain_extensions.split(',')]
        df = df[df['emails'].str.lower().str.endswith(tuple(extensions))]

    # Optionally exclude specific emails
    if exclude_emails:
        exclude_list = [email.strip().lower() for email in exclude_emails.split(',')]
        # Use a lambda function to check for partial matches in the exclusion list
        df = df[~df['emails'].apply(lambda x: any(email in x.lower() for email in exclude_list))]

    # Remove duplicates and sort emails
    df['emails'] = df['emails'].str.lower()
    df = df.drop_duplicates(subset=['emails'])
    df = df.sort_values(by=['emails'])

    # Save the extracted emails to the output file
    if not output_file.lower().endswith(('.xlsx', '.csv', '.txt')):
        error_message = "Error: The output file should have .xlsx, .csv, or .txt extension."
        logging.error(error_message)
        print(RED + error_message + RESET)
        return

    try:
        # Format the output file to avoid extra line breaks and spaces
        df.to_csv(output_file, index=False, header=True)
        success_message = f"\nExtracted emails have been saved to '{output_file}'."
        print(GREEN + success_message + RESET)
    except Exception as e:
        error_message = f"Error while saving the output file: {str(e)}"
        logging.error(error_message)
        print(RED + error_message + RESET)

if __name__ == "__main__":
    input_file = input("Enter the name of the file to extract emails from (e.g. input.xlsx, input.csv, input.txt): ")
    output_file = input("Enter the name of the output file to save the extracted emails: ")
    domain_extensions = input("Enter the email domain extensions to extract (e.g. gmail.com, edu - optional, separated by commas, press Enter to skip): ")
    exclude_emails = input("Enter the email addresses to exclude (e.g. gmail.com, edu - optional, separated by commas, press Enter to include all): ")

    try:
        extract_emails_from_file(input_file, output_file, domain_extensions, exclude_emails)
    except Exception as e:
        error_message = f"An unexpected error occurred: {str(e)}"
        logging.error(error_message)
        print(RED + error_message + RESET)
