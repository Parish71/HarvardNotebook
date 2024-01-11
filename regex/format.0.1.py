# the goal of which is to reformat the user's input in the format we expect.
# amazing for data cleaning

name = input("Whats's your name? ").strip()
if "," in name:
    last, first = name.split(", ")
    name = f"{first} {last}"
print(f"hello, {name}")

