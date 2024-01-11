import re

email = input("What's your email? ").strip()

#In this case, r indicates a raw string
if re.search(r".+@.+\.edu", email):
    print("Valid")
else:
    print("Invalid")

