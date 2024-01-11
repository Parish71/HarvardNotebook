# implementing ^and $ at the re

import re

email = input("What's your email? ")

if re.search(r"^.+@.+\.edu$",email):
    print("Valid")
else:
    print("Invalid")

