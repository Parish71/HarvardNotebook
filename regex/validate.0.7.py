# implementing the [] at the re

# [a-zA-Z0-9_] == \w

import re

email = input("What's your email? ")

if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$",email):
    print("Valid")
else:
    print("Invalid")

