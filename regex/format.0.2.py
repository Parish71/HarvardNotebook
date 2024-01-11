# the goal of which is to reformat the user's input in the format we expect.
# amazing for data cleaning
import re

name = input("Whats's your name? ").strip()
matches = re.search(r"^(.+), (.+)$", name)

if matches:
    last = matches.group(1)
    first = matches.group(2)
    name = f"{first} {last}
print(f"hello, {name}")
