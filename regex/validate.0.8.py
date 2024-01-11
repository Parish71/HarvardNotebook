# Using Flags

import re

email = input("What's your email? ")

if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$",email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")

