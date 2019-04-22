#! python3

import re, pyperclip

# Create regex for phone number
phoneRegex = re.compile(r'''
(
# 415-555-2222, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345
((\d\d\d) | (\(\d\d\d\)))? # AREA CODE(Optional)
(\s| -) # first separator (Optional)
(\d\d\d) # first three digits
(\s| -) # second separator
(\d{4}) # last 4 digits
(((ext(\.)?\s)|x) # extension word part
 (\d{2,5}))? # extension number part.
)
''', re.VERBOSE)

# Create regex for email addresses
emailRegex = re.compile(r'''
[a-zA-Z0-9+_.]+ # name part
@               # @ symbol
[a-zA-Z0-9+_.]+ # domain name part
''', re.VERBOSE)


# Get the text off the clipboard
text = pyperclip.paste()

# Extract email /phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])


# Copy extracted email/phone to the clipboard.
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)
