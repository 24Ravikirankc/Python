# Read an ASCII string from the user
ascii_string = input("Enter an ASCII string: ")

# Convert the ASCII string to a bytes object using UTF-8 encoding
utf8_encoded = ascii_string.encode('utf-8')

# Optionally, decode back to Unicode string
unicode_string = utf8_encoded.decode('utf-8')

# Display the results
print("UTF-8 encoded bytes:", utf8_encoded)
print("Unicode string:", unicode_string)
# unicodeString = u"hello world!"
# print(unicodeString)