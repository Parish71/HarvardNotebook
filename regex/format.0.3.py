import re

name = input("Whats's your name? ").strip()
matches = re.search(r"^(.+), *(.+)$", name)

if matches:
    name = matches.group(2) + " " + matches.group(1)
print (f"hello, {name}")

