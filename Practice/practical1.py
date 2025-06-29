# Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the company name of a given email address. Both user names and company names are composed of letters only. 
# Example: If the following email address is given as input to the program: john@google.com

# Get email input from the user
email = input("Enter an email address: ")

# Split the email to extract the company name
company_name = email.split('@')[1].split('.')[0]

# Print the company name
print("Company name:", company_name)
