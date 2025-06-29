# Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the user name of a given email address. Both user names and company names are composed of letters only.
# Get email input from the user
email = input("Enter an email address: ")

# Extract the username (portion before '@')
username = email.split('@')[0]

# Print the username
print("Username:", username)
