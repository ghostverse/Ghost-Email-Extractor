The "ghostEmailExtractor" script is a practical tool designed for businesses to streamline the extraction of relevant email addresses from text-based documents. With a focus on simplicity and user-friendliness, the script efficiently processes input files, identifies email addresses using regular expressions, and provides customization options such as filtering by domain extensions or excluding specific emails. The script's capabilities include handling duplicate entries, sorting the final list alphabetically, and saving the results in various file formats like CSV and Excel. By offering a straightforward command-line interface, the tool enhances email data management, supporting businesses in organizing and utilizing contact information effectively.

#Features

1. **Email Extraction:** Extracts email addresses from a specified input file.
  
2. **Input Validation:** Checks if the input file exists before processing.

3. **Logging:** Logs errors to a file named 'error.txt'.

4. **Data Storage:** Uses Pandas DataFrame to store extracted emails.

5. **Filtering by Domain Extensions:** Optionally filters emails by specified domain extensions.

6. **Exclusion of Specific Emails:** Optionally excludes specific email addresses.

7. **Duplicate Removal:** Removes duplicate email addresses.

8. **Sorting:** Sorts the final list of emails alphabetically.

9. **Output File Formats:** Saves the extracted emails to CSV, Excel, or text files.

10. **User Interaction:** Prompts the user for input, including file names and optional parameters.

11. **User Feedback:** Provides informative messages to the user about the extraction process.

12. **Exception Handling:** Handles unexpected errors and displays error messages.

13. **User-Friendly Prompts:** Presents clear and user-friendly prompts for input.

14. To run this script use this command (without the quotation marks) ==> "python3 ghostEmailExtractor.py"

15. Ensure that The email address list begins with ==> "Email" before your email addresses to avoid any error (without the quotation marks).
